from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Tuple
from collections import Counter
from itertools import combinations

import sys

# ============================================================================
# 기본 구조 (제공된 코드)
# ============================================================================

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

@dataclass
class Bid:
    group: str
    amount: int

@dataclass
class DicePut:
    rule: DiceRule
    dice: List[int]

class GameState:
    def __init__(self):
        self.dice: List[int] = []
        self.rule_score: List[Optional[int]] = [None] * 12
        self.bid_score = 0

    def get_total_score(self) -> int:
        basic = sum(score for score in self.rule_score[0:6] if score is not None)
        bonus = 35000 if basic >= 63000 else 0
        combination = sum(score for score in self.rule_score[6:12] if score is not None)
        return basic + bonus + combination + self.bid_score

    def bid(self, is_successful: bool, amount: int):
        self.bid_score += -amount if is_successful else amount

    def add_dice(self, new_dice: List[int]):
        self.dice.extend(new_dice)

    def use_dice(self, put: DicePut):
        assert put.rule is not None and self.rule_score[put.rule.value] is None, "Rule already used"
        for d in put.dice:
            self.dice.remove(d)
        assert put.rule is not None
        self.rule_score[put.rule.value] = self.calculate_score(put)

    # ============================================================================
    # [개선] 점수 계산 로직: 더 효율적이고 간결한 코드로 수정
    # ============================================================================
    @staticmethod
    def calculate_score(put: DicePut) -> int:
        rule, dice = put.rule, put.dice
        counts = Counter(dice)
        total_sum = sum(dice)

        if rule == DiceRule.ONE: return counts.get(1, 0) * 1000
        if rule == DiceRule.TWO: return counts.get(2, 0) * 2000
        if rule == DiceRule.THREE: return counts.get(3, 0) * 3000
        if rule == DiceRule.FOUR: return counts.get(4, 0) * 4000
        if rule == DiceRule.FIVE: return counts.get(5, 0) * 5000
        if rule == DiceRule.SIX: return counts.get(6, 0) * 6000
        if rule == DiceRule.CHOICE: return total_sum * 1000
        
        if rule == DiceRule.FOUR_OF_A_KIND:
            return total_sum * 1000 if any(c >= 4 for c in counts.values()) else 0
        
        if rule == DiceRule.FULL_HOUSE:
            return total_sum * 1000 if sorted(counts.values()) in [[2, 3], [5]] else 0
        
        unique_dice = set(dice)
        if rule == DiceRule.SMALL_STRAIGHT:
            for i in range(1, 4):
                if {i, i + 1, i + 2, i + 3}.issubset(unique_dice):
                    return 15000
            return 0
        
        if rule == DiceRule.LARGE_STRAIGHT:
            for i in range(1, 3):
                if {i, i + 1, i + 2, i + 3, i + 4}.issubset(unique_dice):
                    return 30000
            return 0
            
        if rule == DiceRule.YACHT:
            return 50000 if 5 in counts.values() else 0
        
        assert False, "Invalid rule"

class Game:
    def __init__(self):
        self.my_state = GameState()
        self.opp_state = GameState()
    
    # ================================ [AI 두뇌 파트] ================================
    # AI의 모든 전략적 계산을 담당하는 헬퍼 함수
    # ============================================================================
    def _evaluate_potential(self, dice_pool: List[int], player_state: GameState) -> Tuple[Optional[DicePut], float]:
        """
        주어진 주사위 묶음의 '전략적 가치'를 평가하여,
        최적의 (점수 획득 방법, 예상 가치)를 반환합니다.
        """
        available_rules = [DiceRule(i) for i, score in enumerate(player_state.rule_score) if score is None]
        if not available_rules:
            return None, 0.0

        best_move = None
        max_strategic_value = -1e9

        for dice_selection_tuple in set(combinations(sorted(dice_pool), 5)):
            dice_selection = list(dice_selection_tuple)
            for rule in available_rules:
                put = DicePut(rule, dice_selection)
                raw_score = float(GameState.calculate_score(put))
                
                strategic_value = raw_score

                # 전략 1: 희귀 카테고리 낭비 방지
                if raw_score == 0 and rule in [DiceRule.YACHT, DiceRule.LARGE_STRAIGHT, DiceRule.FULL_HOUSE]:
                    strategic_value -= 50000

                # 전략 2: 63k 보너스 가치 반영
                if rule.value <= 5: # ONE ~ SIX
                    current_upper = sum(s for s in player_state.rule_score[:6] if s is not None)
                    if current_upper < 63000 and current_upper + raw_score >= 63000:
                        strategic_value += 35000
                    elif current_upper < 63000:
                        strategic_value += raw_score * 0.5

                if strategic_value > max_strategic_value:
                    max_strategic_value = strategic_value
                    best_move = put
        
        return best_move, max_strategic_value

    # ================================ [필수 구현] ================================
    # ============================================================================
    # [교체된 로직 1] 전략적 입찰 함수
    # ============================================================================
    def calculate_bid(self, dice_a: List[int], dice_b: List[int]) -> Bid:
        # 1. 나의 입장에서 각 묶음의 가치 평가
        _, my_potential_a = self._evaluate_potential(self.my_state.dice + dice_a, self.my_state)
        _, my_potential_b = self._evaluate_potential(self.my_state.dice + dice_b, self.my_state)

        # 2. 상대 입장에서 각 묶음의 가치 추정 (상대 보유 주사위는 모르므로 새 주사위만으로)
        _, opp_potential_a = self._evaluate_potential(dice_a, self.opp_state)
        _, opp_potential_b = self._evaluate_potential(dice_b, self.opp_state)

        my_preference = "A" if my_potential_a > my_potential_b else "B"
        opp_preference = "A" if opp_potential_a > opp_potential_b else "B"

        bid_amount = 0
        if my_preference == opp_preference:
            # 경쟁 발생 시, '한계 이득'(이 묶음을 얻음으로써 추가되는 가치)을 기반으로 입찰가 산정
            my_marginal_gain = abs(my_potential_a - my_potential_b)
            opp_marginal_gain = abs(opp_potential_a - opp_potential_b)
            # 이기는 것과 지는 것의 기대값을 모두 고려한 최적 입찰가
            bid_amount = int(min(my_marginal_gain, opp_marginal_gain) * 0.5 + abs(my_marginal_gain - opp_marginal_gain) * 0.2)

        bid_amount = max(0, min(100000, bid_amount))
        return Bid(my_preference, bid_amount)

    # ============================================================================
    # [교체된 로직 2] 최적 점수 획득 함수
    # ============================================================================
    def calculate_put(self) -> DicePut:
        # 내 현재 보유 주사위 전체를 대상으로 가장 전략적 가치가 높은 수를 찾는다
        best_put, _ = self._evaluate_potential(self.my_state.dice, self.my_state)
        
        # 만약 둘 곳이 없다면(모든 칸 사용) 비상 로직
        if best_put is None:
            rule = DiceRule(next(i for i, score in enumerate(self.my_state.rule_score) if score is None))
            dice = self.my_state.dice[:5]
            return DicePut(rule, dice)

        return best_put
    
    # ============================== [필수 구현 끝] ==============================
    # ============================================================================
    # 상태 업데이트 및 I/O (제공된 코드)
    # ============================================================================
    def update_get(self, dice_a: List[int], dice_b: List[int], my_bid: Bid, opp_bid: Bid, my_group: str):
        if my_group == "A":
            self.my_state.add_dice(dice_a)
            self.opp_state.add_dice(dice_b)
        else:
            self.my_state.add_dice(dice_b)
            self.opp_state.add_dice(dice_a)
        
        my_bid_ok = my_bid.group == my_group
        self.my_state.bid(my_bid_ok, my_bid.amount)

        opp_group = "B" if my_group == "A" else "A"
        opp_bid_ok = opp_bid.group == opp_group
        self.opp_state.bid(opp_bid_ok, opp_bid.amount)

    def update_put(self, put: DicePut):
        self.my_state.use_dice(put)

    def update_set(self, put: DicePut):
        self.opp_state.use_dice(put)

def main():
    game = Game()
    dice_a, dice_b = [0] * 5, [0] * 5
    my_bid = Bid("", 0)

    while True:
        try:
            line = sys.stdin.readline().strip()
            if not line: continue
            
            command, *args = line.split()

            if command == "READY":
                print("OK")
            elif command == "ROLL":
                str_a, str_b = args
                dice_a = [int(c) for c in str_a]
                dice_b = [int(c) for c in str_b]
                my_bid = game.calculate_bid(dice_a, dice_b)
                print(f"BID {my_bid.group} {my_bid.amount}")
            elif command == "GET":
                get_group, opp_group, opp_score = args
                game.update_get(dice_a, dice_b, my_bid, Bid(opp_group, int(opp_score)), get_group)
            elif command == "SCORE":
                put = game.calculate_put()
                game.update_put(put)
                print(f"PUT {put.rule.name} {''.join(map(str, sorted(put.dice)))}")
            elif command == "SET":
                rule_str, dice_str = args
                dice = [int(c) for c in dice_str]
                game.update_set(DicePut(DiceRule[rule_str], dice))
            elif command == "FINISH":
                break
            
            sys.stdout.flush()
        except EOFError:
            break

if __name__ == "__main__":
    main()