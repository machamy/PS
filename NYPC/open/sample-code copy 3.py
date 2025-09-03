from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Tuple, Dict
from itertools import combinations
import sys
import math
import random

# ===== Rules =====
class DiceRule(Enum):
    ONE = 0
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    CHOICE = 6
    FOUR_OF_A_KIND = 7
    FULL_HOUSE = 8
    SMALL_STRAIGHT = 9
    LARGE_STRAIGHT = 10
    YACHT = 11

# ===== IO structs =====
@dataclass
class Bid:
    group: str  # 'A' or 'B'
    amount: int  # 0..100000

@dataclass
class DicePut:
    rule: DiceRule
    dice: List[int]  # 5 dice

# ===== Game State =====
class GameState:
    def __init__(self):
        self.dice: List[int] = []  # carry dice across rounds
        self.rule_score: List[Optional[int]] = [None] * 12
        self.bid_score: int = 0

    def get_total_score(self) -> int:
        basic = sum(s for s in self.rule_score[0:6] if s is not None)
        bonus = 35000 if basic >= 63000 else 0
        combi = sum(s for s in self.rule_score[6:12] if s is not None)
        return basic + bonus + combi + self.bid_score

    def bid(self, is_successful: bool, amount: int):
        if is_successful:
            self.bid_score -= amount
        else:
            self.bid_score += amount

    def add_dice(self, new_dice: List[int]):
        self.dice.extend(new_dice)

    def use_dice(self, put: DicePut):
        assert put.rule is not None and self.rule_score[put.rule.value] is None, "Rule already used"
        for d in put.dice:
            self.dice.remove(d)
        self.rule_score[put.rule.value] = self.calculate_score(put)

    @staticmethod
    def calculate_score(put: DicePut) -> int:
        rule, dice = put.rule, put.dice
        if rule == DiceRule.ONE:
            return sum(d for d in dice if d == 1) * 1000
        if rule == DiceRule.TWO:
            return sum(d for d in dice if d == 2) * 1000
        if rule == DiceRule.THREE:
            return sum(d for d in dice if d == 3) * 1000
        if rule == DiceRule.FOUR:
            return sum(d for d in dice if d == 4) * 1000
        if rule == DiceRule.FIVE:
            return sum(d for d in dice if d == 5) * 1000
        if rule == DiceRule.SIX:
            return sum(d for d in dice if d == 6) * 1000
        if rule == DiceRule.CHOICE:
            return sum(dice) * 1000
        if rule == DiceRule.FOUR_OF_A_KIND:
            ok = any(dice.count(i) >= 4 for i in range(1, 7))
            return sum(dice) * 1000 if ok else 0
        if rule == DiceRule.FULL_HOUSE:
            pair = triple = False
            for i in range(1, 7):
                cnt = dice.count(i)
                if cnt == 2 or cnt == 5:
                    pair = True
                if cnt == 3 or cnt == 5:
                    triple = True
            return sum(dice) * 1000 if pair and triple else 0
        if rule == DiceRule.SMALL_STRAIGHT:
            e = [dice.count(i) > 0 for i in range(1, 7)]
            ok = (e[0] and e[1] and e[2] and e[3]) or (e[1] and e[2] and e[3] and e[4]) or (e[2] and e[3] and e[4] and e[5])
            return 15000 if ok else 0
        if rule == DiceRule.LARGE_STRAIGHT:
            e = [dice.count(i) > 0 for i in range(1, 7)]
            ok = (e[0] and e[1] and e[2] and e[3] and e[4]) or (e[1] and e[2] and e[3] and e[4] and e[5])
            return 30000 if ok else 0
        if rule == DiceRule.YACHT:
            ok = any(dice.count(i) == 5 for i in range(1, 7))
            return 50000 if ok else 0
        assert False, "Invalid rule"

# ===== helpers for counts =====
def to_cnt(v: List[int]) -> List[int]:
    c = [0]*7
    for x in v:
        c[x] += 1
    return c

def cnt_sum(c: List[int]) -> int:
    return sum(i*c[i] for i in range(1,7))

def faces_mask(c: List[int]) -> int:
    m=0
    for f in range(1,7):
        if c[f]>0: m |= (1<<(f-1))
    return m

def pick_smallest(c: List[int], need: int) -> List[int]:
    t=[0]*7
    left=need
    for f in range(1,7):
        k=min(c[f],left); t[f]=k; left-=k
        if left==0: break
    return t

def pick_largest(c: List[int], need: int) -> List[int]:
    t=[0]*7
    left=need
    for f in range(6,0,-1):
        k=min(c[f],left); t[f]=k; left-=k
        if left==0: break
    return t

def add_cnt(a: List[int], b: List[int]) -> List[int]:
    return [0, a[1]+b[1], a[2]+b[2], a[3]+b[3], a[4]+b[4], a[5]+b[5], a[6]+b[6]]

def sub_cnt(a: List[int], b: List[int]) -> List[int]:
    return [0, a[1]-b[1], a[2]-b[2], a[3]-b[3], a[4]-b[4], a[5]-b[5], a[6]-b[6]]

def expand_cnt(c: List[int]) -> List[int]:
    v=[]
    for f in range(1,7):
        v += [f]*c[f]
    return v

# ===== immediate scoring primitives (5 dice used) =====
def build_used_upper(allc: List[int], face: int) -> List[int]:
    u=[0]*7
    t=min(allc[face],5); u[face]=t
    need=5-t
    if need>0:
        rest=sub_cnt(allc, u)
        ex=pick_smallest(rest, need)
        u=add_cnt(u, ex)
    return u

def score_upper(allc: List[int], face: int) -> Tuple[int, List[int]]:
    u=build_used_upper(allc, face)
    return (u[face]*face*1000, u)

def score_choice(allc: List[int]) -> Tuple[int, List[int]]:
    u=pick_largest(allc, 5)
    s=sum(f*u[f] for f in range(1,7))*1000
    return (s, u)

def score_four_kind(allc: List[int]) -> Tuple[int, List[int]]:
    best=-1; bu=[0]*7
    for f in range(1,7):
        if allc[f]>=4:
            u=[0]*7; u[f]=4
            rest=sub_cnt(allc,u)
            ex=pick_largest(rest,1)
            u=add_cnt(u,ex)
            s=sum(k*u[k] for k in range(1,7))*1000
            if s>best: best=s; bu=u
    if best<0: # not available
        return (0, pick_smallest(allc,5))
    return (best, bu)

def score_full_house(allc: List[int]) -> Tuple[int, List[int]]:
    best=-1; bu=[0]*7
    for a in range(1,7):
        if allc[a]>=3:
            for b in range(1,7):
                if b==a: continue
                if allc[b]>=2:
                    u=[0]*7; u[a]=3; u[b]=2
                    s=(3*a+2*b)*1000
                    if s>best: best=s; bu=u
            if allc[a]>=5:
                u=[0]*7; u[a]=5
                s=5*a*1000
                if s>best: best=s; bu=u
    if best<0:
        return (0, pick_smallest(allc,5))
    return (best, bu)

def score_small_straight(allc: List[int]) -> Tuple[int, List[int]]:
    m=faces_mask(allc)
    if (m&0x0F)==0x0F or (m&0x1E)==0x1E or (m&0x3C)==0x3C:
        u=[0]*7
        if (m&0x0F)==0x0F: u[1]=u[2]=u[3]=u[4]=1
        elif (m&0x1E)==0x1E: u[2]=u[3]=u[4]=u[5]=1
        else: u[3]=u[4]=u[5]=u[6]=1
        rest=sub_cnt(allc,u)
        ex=pick_smallest(rest,1)
        u=add_cnt(u,ex)
        return (15000,u)
    return (0, pick_smallest(allc,5))

def score_large_straight(allc: List[int]) -> Tuple[int, List[int]]:
    m=faces_mask(allc)
    if (m&0x1F)==0x1F or (m&0x3E)==0x3E:
        u=[0]*7
        if (m&0x1F)==0x1F: u[1]=u[2]=u[3]=u[4]=u[5]=1
        else: u[2]=u[3]=u[4]=u[5]=u[6]=1
        return (30000,u)
    return (0, pick_smallest(allc,5))

def score_yacht(allc: List[int]) -> Tuple[int, List[int], Optional[int]]:
    for f in range(1,7):
        if allc[f]>=5:
            u=[0]*7; u[f]=5
            return (50000, u, f)
    return (0, pick_smallest(allc,5), None)

# ===== 252 states precompute for E_next =====
_STATES5: List[List[int]]=[]
_WEIGHTS5: List[int]=[] # 5!/(n1!...n6!)
def _gen5(face: int, left: int, cur: List[int]):
    FACT=[1,1,2,6,24,120]
    if face==6:
        cur[6]=left
        s = [0]+cur[1:]
        _STATES5.append(s.copy())
        n1,n2,n3,n4,n5,n6 = s[1],s[2],s[3],s[4],s[5],s[6]
        denom = FACT[n1]*FACT[n2]*FACT[n3]*FACT[n4]*FACT[n5]*FACT[n6]
        _WEIGHTS5.append(120//denom)
        return
    for k in range(left+1):
        cur[face]=k
        _gen5(face+1, left-k, cur)

def _precompute_states5():
    _STATES5.clear(); _WEIGHTS5.clear()
    cur=[0]*7
    _gen5(1,5,cur)

# ===== masks helpers =====
def mask_all_unused() -> int:
    return (1<<12)-1

def rule_unused(rem_mask: int, rule: DiceRule) -> bool:
    return (rem_mask & (1<<rule.value)) != 0

# ----- best immediate (now) with redirection + coverage pressure -----
class ImmediateOption:
    __slots__=("score","rule","used","left","effective")
    def __init__(self, score:int, rule:DiceRule, used:List[int], left:List[int], effective:int):
        self.score=score; self.rule=rule; self.used=used; self.left=left; self.effective=effective

def _score_by_rule(allc: List[int], rule: DiceRule) -> Tuple[int, List[int]]:
    if rule==DiceRule.CHOICE: return score_choice(allc)
    if rule==DiceRule.FOUR_OF_A_KIND: return score_four_kind(allc)
    if rule==DiceRule.FULL_HOUSE: return score_full_house(allc)
    if rule==DiceRule.SMALL_STRAIGHT: return score_small_straight(allc)
    if rule==DiceRule.LARGE_STRAIGHT: return score_large_straight(allc)
    if rule==DiceRule.YACHT:
        s,u,_=score_yacht(allc); return s,u
    # upper
    face = rule.value+1
    return score_upper(allc, face)

def _coverage_bonus(rule: DiceRule, score: int, my_state: GameState) -> int:
    """ONE/TWO 제외, 아직 미기록 카테고리를 이번에 >0으로 채우면 보너스."""
    if score<=0: return 0
    if rule in (DiceRule.ONE, DiceRule.TWO): return 0
    if my_state.rule_score[rule.value] is None:
        return 2500  # 가볍게 밀어주기
    return 0

def _zero_risk_penalty(allc_left: List[int], my_state: GameState) -> int:
    """남은 5개만으로는 특정 카테고리가 영영 0으로 남을 위험을 대충 패널티(과하지 않게)."""
    # 간단 휴리스틱: 3/4/5/6 상단에 해당 눈이 하나도 없고, 그 규칙이 비어있으면 페널티
    pen=0
    for face, rule in [(6,DiceRule.SIX),(5,DiceRule.FIVE),(4,DiceRule.FOUR),(3,DiceRule.THREE)]:
        if my_state.rule_score[rule.value] is None and allc_left[face]==0:
            pen += 1200
    return pen

def _upper_drive_bonus(rule: DiceRule, used: List[int], my_state: GameState) -> int:
    """상단 보너스 드라이브: 상단이면 가산."""
    if rule.value<=DiceRule.SIX.value:
        face=rule.value+1
        cnt=used[face]
        # 63k 미만이면 더 크게
        basic_now = sum(s for s in my_state.rule_score[0:6] if s is not None)
        w = 0.8 if basic_now<63000 else 0.3
        return int(w * (face*cnt*1000))
    return 0

def best_immediate_pick(all10: List[int], rem_mask: int, my_state: GameState) -> ImmediateOption:
    """이번 라운드에서 쓸 5개와 규칙을 고른다. 포카/야찌 상단 리디렉션 포함, coverage pressure 반영."""
    options: List[ImmediateOption]=[]
    # 1) 기본 모든 규칙 후보
    for rule in DiceRule:
        if not rule_unused(rem_mask, rule): continue
        s,u = _score_by_rule(all10, rule)
        left = sub_cnt(all10, u)
        # effective 계산
        eff = s + _upper_drive_bonus(rule,u,my_state) + _coverage_bonus(rule,s,my_state) - _zero_risk_penalty(left,my_state)
        options.append(ImmediateOption(s,rule,u,left,eff))

    # 2) 리디렉션: 포카/야찌가 6·5이면 상단으로도 넣는 후보 추가
    # 야찌
    s_y, u_y, face_y = score_yacht(all10)
    if s_y>0 and face_y in (5,6):
        for rule in ([DiceRule.SIX] if face_y==6 else [DiceRule.FIVE]):
            if rule_unused(rem_mask, rule):
                # 상단으로 5개 같은 눈을 꽂아도 규칙상 OK(상단은 해당 눈만 점수 집계됨)
                u=[0]*7; u[face_y]=5
                left=sub_cnt(all10,u)
                s = face_y*5*1000
                eff = s + _upper_drive_bonus(rule,u,my_state) + _coverage_bonus(rule,s,my_state) - _zero_risk_penalty(left,my_state)
                options.append(ImmediateOption(s,rule,u,left,eff))
    # 포카 (4개 동일이 6·5)
    for face in (6,5):
        if all10[face]>=4:
            rule = DiceRule.SIX if face==6 else DiceRule.FIVE
            if rule_unused(rem_mask, rule):
                u=[0]*7; u[face]=min(5, all10[face])  # 4 또는 5(실제론 최대 5 가능)
                need=5-u[face]
                if need>0:
                    rest=sub_cnt(all10,u)
                    ex=pick_smallest(rest,need)
                    u=add_cnt(u,ex)
                left=sub_cnt(all10,u)
                s=u[face]*face*1000
                eff = s + _upper_drive_bonus(rule,u,my_state) + _coverage_bonus(rule,s,my_state) - _zero_risk_penalty(left,my_state)
                options.append(ImmediateOption(s,rule,u,left,eff))

    # 3) 0점 아닌 후보 우선 정렬, 동점이면 effective, 그다음 원점수
    nonzero = [op for op in options if not (op.rule not in (DiceRule.ONE,DiceRule.TWO) and op.score==0)]
    pool = nonzero if nonzero else options
    pool.sort(key=lambda op: (op.score>0, op.effective, op.score), reverse=True)
    best = pool[0]
    return best

# ===== E_next: expected best next-round score =====
def best_immediate_score_only(allc: List[int], rem_mask: int, my_state: GameState) -> int:
    op = best_immediate_pick(allc, rem_mask, my_state)
    return op.score

def E_next(left5: List[int], rem_mask: int, my_state: GameState) -> float:
    # sum over 252 states with exact multinomial weights (denominator 7776)
    num = 0
    for st, w in zip(_STATES5, _WEIGHTS5):
        allc = add_cnt(left5, st)
        sc = best_immediate_score_only(allc, rem_mask, my_state)
        num += sc * w
    return num / 7776.0

# ===== AI Game =====
class Game:
    def __init__(self):
        self.my_state = GameState()
        self.opp_state = GameState()

        # Opponent bidding EMA (aggressiveness)
        self.opp_alpha_ema = 1.0
        self.total_spent = 0

        # parameters
        self.ALPHA_SELF_BASE = 0.95
        self.DELTA_AVOID = 1500
        self.SMALL_DELTA_ZERO = 1200
        self.CAP_COLLISION = 6000
        self.CAP_NONCOLLISION = 12000
        self.ROI_MAX_RATIO = 1.00
        self.BANKROLL_CAP = 75000
        self.BANKROLL_ALPHA_SCL = 0.80
        self.HEDGE_MARGIN_MIN = 400
        self.HEDGE_MARGIN_MAX = 900

        # random zero-bid trickle (to avoid being predictable)
        self.ZERO_BID_P = 0.15  # 15% when conditions met

        _precompute_states5()

    # ====== Required: BID ======
    def calculate_bid(self, dice_a: List[int], dice_b: List[int]) -> Bid:
        my_carry = list(self.my_state.dice)
        opp_carry = list(self.opp_state.dice)

        used_cnt = sum(1 for s in self.my_state.rule_score if s is not None)
        late_phase = used_cnt >= 9

        # bundle VoB
        vA = self._bundle_value(add=to_cnt(dice_a))
        vB = self._bundle_value(add=to_cnt(dice_b))

        # opponent simple VoB (1-step)
        opp_mask = self._unused_mask(self.opp_state)
        vA_opp = self._opp_bundle_value(to_cnt(dice_a), opp_mask)
        vB_opp = self._opp_bundle_value(to_cnt(dice_b), opp_mask)

        # my preference
        choose_A = vA["my_vob"] >= vB["my_vob"]
        chosen_group = "A" if choose_A else "B"
        chosen_eval = vA if choose_A else vB
        other_eval  = vB if choose_A else vA

        # opponent preference
        opp_choose_A = vA_opp >= vB_opp
        gOpp = "A" if opp_choose_A else "B"

        # zero-bid occasional if small delta & collision
        dSelf = abs(vA["my_vob"] - vB["my_vob"])
        dOpp  = abs(vA_opp - vB_opp)

        # "0점 넣느니 입찰로 회피": 이번 최고점이 0이고 다른 쪽 >0이면 강 베이스
        zero_avoid_boost = 0
        if chosen_eval["best_now"] == 0 and other_eval["best_now"] > 0:
            # later rounds: stronger
            rem_rules = len(self._unused_rules_of(self.my_state))
            stage_factor = 1.0 + max(0, 6 - rem_rules) * 0.25
            zero_avoid_boost = int(12000 * stage_factor)

        # collision avoid switch if small diff
        g = chosen_group
        if chosen_group == gOpp and dSelf < self.DELTA_AVOID and zero_avoid_boost == 0:
            g = "B" if chosen_group == "A" else "A"

        # alpha with bankroll
        alpha = self.ALPHA_SELF_BASE
        if self.total_spent >= self.BANKROLL_CAP:
            alpha *= self.BANKROLL_ALPHA_SCL

        base = int(alpha * dSelf)

        # apply zero-avoid boost
        base = max(base, zero_avoid_boost)

        # random zero-bid slot (when collision & tiny diff)
        if g == gOpp and dSelf < self.SMALL_DELTA_ZERO and zero_avoid_boost == 0:
            if random.random() < self.ZERO_BID_P:
                return Bid(g, 0)

        # collision hedging
        raw = base
        if g == gOpp:
            # estimate opponent need
            closeness = 1.0 - abs(dSelf - dOpp)/max(1.0, dSelf + dOpp)
            margin = int(self.HEDGE_MARGIN_MIN + (self.HEDGE_MARGIN_MAX - self.HEDGE_MARGIN_MIN) * max(0.0, min(1.0, closeness)))
            need = int(self.opp_alpha_ema * dOpp + margin)
            # ROI gate
            if need <= self.ROI_MAX_RATIO * dSelf:
                raw = max(raw, need)
            raw = min(raw, self.CAP_COLLISION)
        else:
            raw = min(raw, self.CAP_NONCOLLISION)

        # minimums
        if dSelf >= 800 or zero_avoid_boost > 0:
            raw = max(raw, 5000 if zero_avoid_boost == 0 else 8000)

        amount = max(0, min(100000, raw))
        return Bid(g, amount)

    # ====== Required: PUT ======
    def calculate_put(self) -> DicePut:
        pool = to_cnt(self.my_state.dice)
        op = self._best_now_option(pool)
        dice = expand_cnt(op.used)
        # safety
        if len(dice) < 5:
            rest=sub_cnt(pool, op.used)
            pad=pick_smallest(rest, 5-len(dice))
            used=add_cnt(op.used, pad)
            dice=expand_cnt(used)
        return DicePut(op.rule, dice)

    # ====== Updates ======
    def update_get(self, dice_a: List[int], dice_b: List[int], my_bid: Bid, opp_bid: Bid, my_group: str):
        if my_group == "A":
            self.my_state.add_dice(dice_a)
            self.opp_state.add_dice(dice_b)
        else:
            self.my_state.add_dice(dice_b)
            self.opp_state.add_dice(dice_a)

        self.my_state.bid(my_bid.group == my_group, my_bid.amount)
        opp_group = "B" if my_group == "A" else "A"
        self.opp_state.bid(opp_bid.group == opp_group, opp_bid.amount)

        # update spent if we won our desired bundle
        if my_group == my_bid.group:
            self.total_spent += my_bid.amount

        # update opp aggressiveness EMA using their bid vs their delta
        opp_mask = self._unused_mask(self.opp_state)
        dA = E_next(to_cnt(dice_a), opp_mask, self.opp_state)
        dB = E_next(to_cnt(dice_b), opp_mask, self.opp_state)
        dOpp = abs(dA - dB)
        if dOpp < 1.0: dOpp = 1.0
        ratio = min(2.0, max(0.0, opp_bid.amount / dOpp))
        decay = 0.85
        self.opp_alpha_ema = max(0.5, min(1.8, decay*self.opp_alpha_ema + (1.0-decay)*ratio))

    def update_put(self, put: DicePut):
        self.my_state.use_dice(put)

    def update_set(self, put: DicePut):
        self.opp_state.use_dice(put)

    # ===== VoB helpers =====
    def _unused_rules_of(self, gs: GameState) -> List[DiceRule]:
        return [DiceRule(i) for i, s in enumerate(gs.rule_score) if s is None]

    def _unused_mask(self, gs: GameState) -> int:
        m=0
        for i, s in enumerate(gs.rule_score):
            if s is None: m |= (1<<i)
        return m

    def _upper_soft_signal(self, cnt_all: List[int]) -> float:
        weights = {6:3.0, 5:2.0, 4:1.0, 3:0.7, 2:0.3, 1:0.3}
        val = sum(weights[f]*cnt_all[f]*f for f in range(1,7))
        basic_now = sum(s for s in self.my_state.rule_score[0:6] if s is not None)
        if basic_now < 63000:
            val *= 2.0
        return val * 1000 * 0.015  # κ_upper≈0.015

    def _best_now_option(self, allc: List[int]) -> ImmediateOption:
        rem_mask = self._unused_mask(self.my_state)
        return best_immediate_pick(allc, rem_mask, self.my_state)

    def _bundle_value(self, add: List[int]) -> Dict[str, float]:
        # 1st round? no scoring: VoB = E_next(bundle)
        rem_mask = self._unused_mask(self.my_state)
        if len(self.my_state.dice)==0:
            v = E_next(add, rem_mask, self.my_state)
            # upper soft preference for 1st round as well
            v += self._upper_soft_signal(add)
            return {"my_vob": v, "best_now": 0}

        # otherwise: best now + E_next(left) + soft upper signal
        allc = add_cnt(to_cnt(self.my_state.dice), add)
        op = self._best_now_option(allc)
        rem2 = rem_mask & ~(1<<op.rule.value)
        v = op.score + E_next(op.left, rem2, self.my_state) + self._upper_soft_signal(allc)
        return {"my_vob": v, "best_now": op.score}

    def _opp_bundle_value(self, add: List[int], opp_mask: int) -> float:
        # opponent 1-step expectation: E_next(bundle)
        return E_next(add, opp_mask, self.opp_state)

# ===== Runner =====
def main():
    game = Game()

    dice_a, dice_b = [0] * 5, [0] * 5
    my_bid = Bid("", 0)

    while True:
        try:
            line = input().strip()
            if not line:
                continue

            command, *args = line.split()

            if command == "READY":
                print("OK", flush=True)
                continue

            if command == "ROLL":
                str_a, str_b = args
                for i, c in enumerate(str_a):
                    dice_a[i] = int(c)
                for i, c in enumerate(str_b):
                    dice_b[i] = int(c)
                my_bid = game.calculate_bid(dice_a, dice_b)
                print(f"BID {my_bid.group} {my_bid.amount}", flush=True)
                continue

            if command == "GET":
                get_group, opp_group, opp_score = args
                opp_score = int(opp_score)
                game.update_get(dice_a, dice_b, my_bid, Bid(opp_group, opp_score), get_group)
                continue

            if command == "SCORE":
                put = game.calculate_put()
                game.update_put(put)
                print(f"PUT {put.rule.name} {''.join(map(str, put.dice))}", flush=True)
                continue

            if command == "SET":
                rule, str_dice = args
                dice = [int(c) for c in str_dice]
                game.update_set(DicePut(DiceRule[rule], dice))
                continue

            if command == "FINISH":
                break

            print(f"Invalid command: {command}", file=sys.stderr, flush=True)
            sys.exit(1)

        except EOFError:
            break

if __name__ == "__main__":
    main()
