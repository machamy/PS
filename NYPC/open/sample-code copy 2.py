from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Tuple
from itertools import combinations
import sys


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


# ===== AI Game =====
class Game:
    def __init__(self):
        self.my_state = GameState()
        self.opp_state = GameState()

        # Burn priority (낮을수록 먼저 소모해도 좋음)
        self._burn_priority = {
            DiceRule.ONE: 0,
            DiceRule.TWO: 1,
            DiceRule.YACHT: 2,
            DiceRule.CHOICE: 3,
            DiceRule.LARGE_STRAIGHT: 4,
            DiceRule.SMALL_STRAIGHT: 5,
            DiceRule.FOUR_OF_A_KIND: 6,
            DiceRule.FULL_HOUSE: 6,
            DiceRule.THREE: 7,
            DiceRule.FOUR: 8,
            DiceRule.FIVE: 9,
            DiceRule.SIX: 10,
        }

    # ====== Required: BID ======
    def calculate_bid(self, dice_a: List[int], dice_b: List[int]) -> Bid:
        my_carry = list(self.my_state.dice)
        opp_carry = list(self.opp_state.dice)

        used_cnt = sum(1 for s in self.my_state.rule_score if s is not None)
        late_phase = used_cnt >= 9
        opp_lambda = 0.5 if late_phase else 0.35

        v_a = self._bundle_value(my_carry + dice_a, self._opp_bundle_estimate(opp_carry + dice_b), late_phase)
        v_b = self._bundle_value(my_carry + dice_b, self._opp_bundle_estimate(opp_carry + dice_a), late_phase)

        if v_a["my_vob"] - opp_lambda * v_a["opp_vob"] >= v_b["my_vob"] - opp_lambda * v_b["opp_vob"]:
            chosen = "A"; chosen_pack = dice_a; chosen_eval = v_a; other_eval = v_b
        else:
            chosen = "B"; chosen_pack = dice_b; chosen_eval = v_b; other_eval = v_a

        me, opp = self.my_state.get_total_score(), self.opp_state.get_total_score()
        diff = opp - me
        delta = max(0, (chosen_eval["my_vob"] - chosen_eval["opp_lambda"] * chosen_eval["opp_vob"])
                    - (other_eval["my_vob"] - other_eval["opp_lambda"] * other_eval["opp_vob"]))

        base = int(0.6 * delta)

        # --- [NEW] 0점 회피 강화 ---
        # 이번 SCORE에서 선택 번들의 최고점이 0이고, 다른 번들은 0보다 크면 강하게 베팅
        rem_rules = len(self._unused_rules_of(self.my_state))
        zero_avoid_boost = 0
        if chosen_eval["best_score"] == 0 and other_eval["best_score"] > 0:
            # 라운드 후반일수록(남은 규칙 적을수록) 더 크게
            # rem_rules: 12(초반) -> 1(막판) 기준으로 보정
            stage_factor = max(1.0, 1.0 + (max(0, 6 - rem_rules) * 0.25))  # 남은 규칙 ≤6부터 가파르게
            # 최소 바닥선 잡고, 가중
            zero_avoid_boost = int(12000 * stage_factor)
            base = max(base, zero_avoid_boost)

        # 둘 다 0이면 굳이 돈 쓰지 말자 (아끼고 ONE/TWO를 태운다)
        if chosen_eval["best_score"] == 0 and other_eval["best_score"] == 0:
            base = 0

        # 야추 즉시 가능 시 강하게
        yacht_now = self._can_make_yacht_now(my_carry + chosen_pack)
        if yacht_now:
            base = max(base, 30000)
            base = min(base + 20000, 40000)

        # SIX 3개 이상 + SIX 미사용이면 소가산
        if chosen_pack.count(6) >= 3 and self.my_state.rule_score[DiceRule.SIX.value] is None:
            base += 3000

        # 스코어 열세일수록 공격적으로
        scale = 1.0 + max(-0.3, min(0.6, (opp - me) / 100000.0))
        amount = int(base * scale)

        # 하한/무의미 차단: 0회피 상황이면 delta가 작아도 어느 정도는 쓴다
        if delta >= 8000 or zero_avoid_boost > 0:
            amount = max(amount, 5000 if zero_avoid_boost == 0 else 8000)

        amount = max(0, min(100000, amount))
        return Bid(chosen, amount)

    # ====== Required: PUT ======
    def calculate_put(self) -> DicePut:
        pool = list(self.my_state.dice)
        score, rule, dice = self._evaluate_best_put(pool)
        if rule is None:
            rule_idx = next(i for i, s in enumerate(self.my_state.rule_score) if s is None)
            rule = DiceRule(rule_idx)
            dice = pool[:5] if len(pool) >= 5 else pool[:]
        return DicePut(rule, dice)

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

    def update_put(self, put: DicePut):
        self.my_state.use_dice(put)

    def update_set(self, put: DicePut):
        self.opp_state.use_dice(put)

    # ====== Internals: Bundle Value ======
    def _bundle_value(self, my_pool: List[int], opp_pool_for_other: List[int], late_phase: bool) -> dict:
        best_score, best_rule, best_dice = self._evaluate_best_put(my_pool)

        alpha = 0.35
        upper_prog = self._upper_progress_value(my_pool)

        beta = 0.8
        yacht_pot = self._yacht_potential(my_pool)

        gamma = 0.25
        straight_pot = self._straight_potential(my_pool)

        delta = 0.2
        quad_fh_pot = self._quad_fullhouse_potential(my_pool)

        opp_lambda = 0.5 if late_phase else 0.35
        opp_vob = self._opp_value_estimate(opp_pool_for_other, late_phase)

        my_vob = best_score + alpha * upper_prog + beta * yacht_pot + gamma * straight_pot + delta * quad_fh_pot
        return {
            "my_vob": my_vob,
            "opp_vob": opp_vob,
            "opp_lambda": opp_lambda,
            "best_score": best_score,   # ← 추가
    }

    def _opp_bundle_estimate(self, pool: List[int]) -> List[int]:
        return pool

    def _opp_value_estimate(self, pool: List[int], late_phase: bool) -> float:
        score, _, _ = self._evaluate_best_put_vs(pool, self._unused_rules_of(self.opp_state), self_bias=False)
        return (score
                + 0.25 * self._upper_progress_value(pool, for_self=False)
                + 0.5 * self._yacht_potential(pool)
                + 0.15 * self._straight_potential(pool)
                + 0.12 * self._quad_fullhouse_potential(pool))

    # ====== Internals: Evaluators ======
    def _unused_rules_of(self, gs: GameState) -> List[DiceRule]:
        return [DiceRule(i) for i, s in enumerate(gs.rule_score) if s is None]

    def _current_basic_sum(self) -> int:
        return sum(s for s in self.my_state.rule_score[0:6] if s is not None)

    def _evaluate_best_put(self, pool: List[int]) -> Tuple[int, Optional[DiceRule], List[int]]:
        return self._evaluate_best_put_vs(pool, self._unused_rules_of(self.my_state), self_bias=True)

    def _evaluate_best_put_vs(self, pool: List[int], unused_rules: List[DiceRule], self_bias: bool = False) -> Tuple[int, Optional[DiceRule], List[int]]:
        n = len(pool)
        if n < 5 or not unused_rules:
            return (0, None, [])
        basic_sum_now = self._current_basic_sum() if self_bias else 0
        want_upper = (basic_sum_now < 63000) if self_bias else False

        # 현재 풀의 얼굴 개수
        pool_counts = [0] + [pool.count(f) for f in range(1, 7)]  # 1..6 인덱싱
        # 상단 채우기 목표(6,5,4,3) 중 아직 4개 미만이면 "보존 대상"
        need_high = {6: pool_counts[6] < 4, 5: pool_counts[5] < 4, 4: pool_counts[4] < 4, 3: pool_counts[3] < 4}
        any_need = any(need_high.values())

        best_effective = -10**9
        best_score = -1
        best_rule: Optional[DiceRule] = None
        best_dice: List[int] = []

        for comb in combinations(range(n), 5):
            dice5 = [pool[i] for i in comb]
            # 기본 점수
            for rule in unused_rules:
                base_score = GameState.calculate_score(DicePut(rule, dice5))
                effective = base_score

                if self_bias:
                    # 1) 상단 가중: 상단이면 가중 크게 (보너스 전이면 더 크게)
                    if rule.value <= DiceRule.SIX.value:
                        face = rule.value + 1
                        cnt = dice5.count(face)
                        upper_w = 0.8 if want_upper else 0.3
                        effective += int(upper_w * (face * cnt * 1000))

                    # 2) 보존/버리기 보너스: 6/5/4/3 보존, 1/2(+조건부 3/4) 버리기
                    if any_need:
                        # 보존(고점) 페널티
                        high_penalty_w = {6: 12000, 5: 9000, 4: 6000, 3: 4000}
                        for f in (6, 5, 4, 3):
                            if need_high[f]:
                                used = dice5.count(f)
                                if used:
                                    effective -= high_penalty_w[f] * used
                        # 버리기(저점) 보너스
                        low_bonus_w = {1: 5000, 2: 3000, 3: 1500, 4: 800}
                        for f in (1, 2, 3, 4):
                            # 3,4는 해당 얼굴이 더 이상 필요하지 않을 때만 버리기 보너스
                            if f in (3, 4) and need_high[f]:
                                continue
                            used = dice5.count(f)
                            if used:
                                effective += low_bonus_w[f] * used

                # 동점은 소프트 타이브레이커
                if effective > best_effective or (effective == best_effective and base_score > best_score):
                    best_effective = effective
                    best_score = base_score
                    best_rule = rule
                    best_dice = dice5

        return (max(0, best_score), best_rule, best_dice)

    # ===== Potentials / Heuristics =====
    def _upper_progress_value(self, pool: List[int], for_self: bool = True) -> float:
        weights = {6: 3.0, 5: 2.0, 4: 1.0, 3: 0.5, 2: 0.5, 1: 0.5}
        val = 0.0
        for face in range(1, 7):
            val += weights.get(face, 0.5) * pool.count(face) * face
        if for_self:
            basic_sum_now = self._current_basic_sum()
            if basic_sum_now < 63000:
                val *= 2.0
        return val * 1000 * 0.01

    def _yacht_potential(self, pool: List[int]) -> float:
        counts = [pool.count(i) for i in range(1, 7)]
        if max(counts) >= 5:
            return 50000
        if max(counts) == 4:
            return 15000
        if max(counts) == 3:
            return 5000
        return 0.0

    def _straight_potential(self, pool: List[int]) -> float:
        s = set(pool)
        large = ({1,2,3,4,5}.issubset(s) or {2,3,4,5,6}.issubset(s))
        if large:
            return 8000
        small = any(set(seq).issubset(s) for seq in [(1,2,3,4), (2,3,4,5), (3,4,5,6)])
        return 3000 if small else 0.0

    def _quad_fullhouse_potential(self, pool: List[int]) -> float:
        top5_sum = sum(sorted(pool, reverse=True)[:5]) * 1000 / 1000.0
        counts = [pool.count(i) for i in range(1, 7)]
        if max(counts) >= 4:
            return top5_sum * 0.3
        have3 = any(c >= 3 for c in counts)
        have2 = any(c >= 2 for c in counts)
        if have3 and have2:
            return top5_sum * 0.15
        return 0.0

    def _can_make_yacht_now(self, pool: List[int]) -> bool:
        counts = [pool.count(i) for i in range(1, 7)]
        return max(counts) >= 5


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
