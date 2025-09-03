from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Tuple
from itertools import combinations
import sys


# 가능한 주사위 규칙들을 나타내는 enum
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


# 입찰 방법을 나타내는 데이터클래스
@dataclass
class Bid:
    group: str  # 입찰 그룹 ('A' 또는 'B')
    amount: int  # 입찰 금액


# 주사위 배치 방법을 나타내는 데이터클래스
@dataclass
class DicePut:
    rule: DiceRule  # 배치 규칙
    dice: List[int]  # 배치할 주사위 목록


# 팀의 현재 상태를 관리하는 클래스
class GameState:
    def __init__(self):
        self.dice: List[int] = []  # 현재 보유한 주사위 목록 (라운드 간 carry)
        self.rule_score: List[Optional[int]] = [None] * 12  # 각 규칙별 획득 점수
        self.bid_score: int = 0  # 입찰로 얻거나 잃은 총 점수

    def get_total_score(self) -> int:
        """현재까지 획득한 총 점수 계산 (상단/하단 점수 + 보너스 + 입찰 점수)"""
        basic = sum(score for score in self.rule_score[0:6] if score is not None)
        bonus = 35000 if basic >= 63000 else 0
        combination = sum(score for score in self.rule_score[6:12] if score is not None)
        return basic + bonus + combination + self.bid_score

    def bid(self, is_successful: bool, amount: int):
        """입찰 결과에 따른 점수 반영"""
        if is_successful:
            self.bid_score -= amount  # 성공시 베팅 금액만큼 점수 차감
        else:
            self.bid_score += amount  # 실패시 베팅 금액만큼 점수 획득

    def add_dice(self, new_dice: List[int]):
        """새로운 주사위들을 보유 목록에 추가"""
        self.dice.extend(new_dice)

    def use_dice(self, put: DicePut):
        """주사위를 사용하여 특정 규칙에 배치"""
        # 이미 사용한 규칙인지 확인
        assert (
            put.rule is not None and self.rule_score[put.rule.value] is None
        ), "Rule already used"

        # 선택한 5개 주사위를 제거
        for d in put.dice:
            self.dice.remove(d)

        # 해당 규칙의 점수 계산 및 저장
        assert put.rule is not None
        self.rule_score[put.rule.value] = self.calculate_score(put)

    @staticmethod
    def calculate_score(put: DicePut) -> int:
        """규칙에 따른 점수를 계산하는 함수"""
        rule, dice = put.rule, put.dice

        # 기본 규칙 점수 계산 (해당 숫자에 적힌 수의 합 × 1000점)
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
        if rule == DiceRule.CHOICE:  # 주사위에 적힌 모든 수의 합 × 1000점
            return sum(dice) * 1000
        if (
            rule == DiceRule.FOUR_OF_A_KIND
        ):  # 같은 수가 적힌 주사위가 4개 있다면 합 × 1000점, 아니면 0
            ok = any(dice.count(i) >= 4 for i in range(1, 7))
            return sum(dice) * 1000 if ok else 0
        if (
            rule == DiceRule.FULL_HOUSE
        ):  # 3개 같은 수 + 2개 같은 수면 합 × 1000점, 아니면 0점
            pair = triple = False
            for i in range(1, 7):
                cnt = dice.count(i)
                # 5개 모두 같아도 인정
                if cnt == 2 or cnt == 5:
                    pair = True
                if cnt == 3 or cnt == 5:
                    triple = True
            return sum(dice) * 1000 if pair and triple else 0
        if (
            rule == DiceRule.SMALL_STRAIGHT
        ):  # 1234, 2345, 3456 중 하나를 포함하면 15000점
            e1, e2, e3, e4, e5, e6 = [dice.count(i) > 0 for i in range(1, 7)]
            ok = (
                (e1 and e2 and e3 and e4)
                or (e2 and e3 and e4 and e5)
                or (e3 and e4 and e5 and e6)
            )
            return 15000 if ok else 0
        if (
            rule == DiceRule.LARGE_STRAIGHT
        ):  # 12345 또는 23456이면 30000점
            e1, e2, e3, e4, e5, e6 = [dice.count(i) > 0 for i in range(1, 7)]
            ok = (e1 and e2 and e3 and e4 and e5) or (e2 and e3 and e4 and e5 and e6)
            return 30000 if ok else 0
        if (
            rule == DiceRule.YACHT
        ):  # 5개 모두 같으면 50000점
            ok = any(dice.count(i) == 5 for i in range(1, 7))
            return 50000 if ok else 0

        assert False, "Invalid rule"


# 게임 상태를 관리하는 클래스
class Game:
    def __init__(self):
        self.my_state = GameState()   # 내 팀의 현재 상태
        self.opp_state = GameState()  # 상대 팀의 현재 상태

        # "버려도 좋은" 순서(낮을수록 먼저 소모해도 좋은 규칙)
        # 사용자가 제안한 우선순위를 반영:
        # ONE, TWO, YACHT, CHOICE, LARGE_STRAIGHT, SMALL_STRAIGHT, FOUR_OF_A_KIND/FULL_HOUSE
        # (상단 3~6은 63,000 보너스 때문에 가급적 아껴서 높은 우선순위 숫자 부여)
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

    # ================================ [필수 구현] ================================
    # ============================================================================

    def calculate_bid(self, dice_a: List[int], dice_b: List[int]) -> Bid:
        """
        입찰 단계에서 A/B 중 어떤 묶음을 가져올지와 금액을 결정.
        전략:
          1) 현재 보유 주사위(self.my_state.dice) + 후보 묶음을 합친 풀로
             이번 SCORE에서 낼 수 있는 최댓값을 시뮬레이션(탐욕X, 전수).
          2) 그 기대값이 더 큰 쪽을 선택.
          3) 금액은 (두 기대값 차이)에 비례 + 상황 보정.
             - YACHT가 가능한 묶음이면 최대 4만까지 강하게 배팅.
             - 6이 3개 이상 포함된 묶음은 상단 보너스 관점에서 가중치(+).
             - 점수 열세일수록 공격적으로, 리드할수록 보수적으로.
        """
        # 내 현재 carry 주사위
        carry = list(self.my_state.dice)

        # 각 후보 풀 구성
        pool_a = carry + dice_a
        pool_b = carry + dice_b

        # 각 풀에서 이번 SCORE에 최선의 선택을 가정하고 평가
        best_a = self._evaluate_best_put(pool_a)
        best_b = self._evaluate_best_put(pool_b)

        # 더 가치 높은 쪽을 선택
        if best_a[0] > best_b[0]:
            chosen_group = "A"
            chosen_best = best_a
            other_best = best_b
            chosen_dice_group = dice_a
        else:
            chosen_group = "B"
            chosen_best = best_b
            other_best = best_a
            chosen_dice_group = dice_b

        # 금액 책정
        my_total = self.my_state.get_total_score()
        opp_total = self.opp_state.get_total_score()
        diff = opp_total - my_total  # 내가 뒤지면 양수

        # 두 후보의 기대 점수 차이 (점수 단위는 포인트, 1000점 단위는 아님)
        delta = max(0, chosen_best[0] - other_best[0])

        # 기본 베팅: 기대값 차이의 60% 정도
        base = int(delta * 0.6)

        # YACHT 강제 강화: 선택한 5개가 YACHT 가능이면 상한 4만 내에서 상향
        # (사용자 제안: "YACHT이 나오면 최대한 많은 점수를 투자해서 가져가(최대 4만)")
        yacht_boost = 0
        if chosen_best[1] == DiceRule.YACHT:
            yacht_boost = 20000  # 기본적으로 2만 보정
            base = max(base, 30000)  # 최소 3만 이상은 베팅 의지
            base = min(base + yacht_boost, 40000)

        # 6이 3개 이상 포함된 묶음(상단 보너스 관점 중요) -> 소폭 가산
        if chosen_dice_group.count(6) >= 3 and self.my_state.rule_score[DiceRule.SIX.value] is None:
            base += 3000

        # 내가 뒤지면 공격적, 앞서면 보수적 (스케일링 0.7~1.6)
        scale = 1.0 + max(-0.3, min(0.6, diff / 100000.0))
        amount = int(base * scale)

        # 너무 작은 금액 방지: 의미 있는 상황이면 하한선 적용
        if delta >= 8000:
            amount = max(amount, 5000)

        # 과도한 금액 억제
        amount = max(0, min(100000, amount))

        return Bid(chosen_group, amount)

    def calculate_put(self) -> DicePut:
        """
        점수 획득 단계: 현재 보유 주사위(보통 10개) 중 5개와 규칙 하나를 선택.
        구현:
          - 가능한 5개 조합 × 사용 가능한 규칙 전수 탐색.
          - 원점수 최대를 우선.
          - 동점 시:
              (a) 상단 보너스 달성에 도움이 되는 상단 규칙(특히 6,5,4)을 선호.
              (b) 그래도 동점이면 '버려도 좋은 순서'를 따라 규칙을 소비.
        """
        pool = list(self.my_state.dice)
        score, rule, dice = self._evaluate_best_put(pool)
        # 사용 가능한 규칙이 없을 리는 없지만, 안전망
        if rule is None:
            # 남은 첫 규칙 + 앞의 5개
            rule_idx = next(i for i, s in enumerate(self.my_state.rule_score) if s is None)
            rule = DiceRule(rule_idx)
            dice = pool[:5] if len(pool) >= 5 else pool[:]
        return DicePut(rule, dice)

    # ============================== [필수 구현 끝] ==============================

    # --- 게임 진행 중 상태 업데이트 ---

    def update_get(
        self,
        dice_a: List[int],
        dice_b: List[int],
        my_bid: Bid,
        opp_bid: Bid,
        my_group: str,
    ):
        """입찰 결과를 받아서 상태 업데이트"""
        # 그룹에 따라 주사위 분배
        if my_group == "A":
            self.my_state.add_dice(dice_a)
            self.opp_state.add_dice(dice_b)
        else:
            self.my_state.add_dice(dice_b)
            self.opp_state.add_dice(dice_a)

        # 입찰 결과에 따른 점수 반영
        my_bid_ok = my_bid.group == my_group
        self.my_state.bid(my_bid_ok, my_bid.amount)

        opp_group = "B" if my_group == "A" else "A"
        opp_bid_ok = opp_bid.group == opp_group
        self.opp_state.bid(opp_bid_ok, opp_bid.amount)

    def update_put(self, put: DicePut):
        """내가 주사위를 배치한 결과 반영"""
        self.my_state.use_dice(put)

    def update_set(self, put: DicePut):
        """상대가 주사위를 배치한 결과 반영"""
        self.opp_state.use_dice(put)

    # --- 내부 유틸리티 ---

    def _unused_rules(self) -> List[DiceRule]:
        return [DiceRule(i) for i, s in enumerate(self.my_state.rule_score) if s is None]

    def _current_basic_sum(self) -> int:
        """상단(ONE~SIX) 합"""
        return sum(s for s in self.my_state.rule_score[0:6] if s is not None)

    def _evaluate_best_put(self, pool: List[int]) -> Tuple[int, Optional[DiceRule], List[int]]:
        """
        주어진 주사위 pool(길이 5 또는 10)에서
        사용 가능한 규칙들 중 이번에 낼 수 있는 최적의 (점수, 규칙, 주사위5개)를 반환.
        점수는 원점수를 기본으로 하되, 동점일 때 tie-break 정책을 적용.
        """
        unused = self._unused_rules()
        n = len(pool)
        if n < 5 or not unused:
            return (0, None, [])

        # 사전 계산
        basic_sum_now = self._current_basic_sum()
        want_upper = basic_sum_now < 63000

        best_score = -1
        best_rule: Optional[DiceRule] = None
        best_dice: List[int] = []

        # 전수 탐색: 5개 조합 × 규칙
        for comb in combinations(range(n), 5):
            dice5 = [pool[i] for i in comb]

            # 약한 휴리스틱: 6이 3개 이상이면 상단 SIX를 우선 고려해 보지만
            # 최종 선택은 전체 비교로 결정.
            count6 = dice5.count(6)

            for rule in unused:
                score = GameState.calculate_score(DicePut(rule, dice5))

                # 동점 시 tie-break용 보조 점수 계산
                tie_bonus = 0

                # (a) 상단 보너스 추구: 상단 규칙이고 높은 눈일수록 약간 가산
                if rule.value <= DiceRule.SIX.value:
                    # face 값 × 개수 × 소보정
                    face = rule.value + 1  # ONE=1, ..., SIX=6
                    cnt = dice5.count(face)
                    # 63k 달성이 아직이면 조금 더 가산
                    tie_bonus += cnt * face * (60 if want_upper else 30)

                # (b) 버려도 좋은 규칙을 소모하는 쪽을 가산(낮은 priority일수록 더 가산)
                tie_bonus += (11 - self._burn_priority.get(rule, 5)) * 5

                # 최종 비교 키
                # 1순위: 원점수, 2순위: tie_bonus
                key = (score, tie_bonus)

                best_key = (
                    best_score,
                    (0 if best_rule is None else (0)),  # placeholder; not used directly
                )

                if score > best_score:
                    best_score = score
                    best_rule = rule
                    best_dice = dice5
                elif score == best_score:
                    # tie-break: 현재 후보 vs 기존 best
                    # 기존 best의 tie_bonus를 재계산해야 공정 비교 가능
                    if best_rule is None:
                        pass
                    else:
                        # 기존 best의 tie_bonus 재계산
                        prev_face_bonus = 0
                        if best_rule.value <= DiceRule.SIX.value:
                            face_prev = best_rule.value + 1
                            cnt_prev = best_dice.count(face_prev)
                            prev_face_bonus += cnt_prev * face_prev * (60 if want_upper else 30)
                        prev_tie_bonus = prev_face_bonus + (11 - self._burn_priority.get(best_rule, 5)) * 5

                        if tie_bonus > prev_tie_bonus:
                            best_rule = rule
                            best_dice = dice5

        return (max(0, best_score), best_rule, best_dice)


def main():
    game = Game()

    # 입찰 라운드에서 나온 주사위들
    dice_a, dice_b = [0] * 5, [0] * 5
    # 내가 마지막으로 한 입찰 정보
    my_bid = Bid("", 0)

    while True:
        try:
            line = input().strip()
            if not line:
                continue

            command, *args = line.split()

            if command == "READY":
                # 게임 시작
                print("OK", flush=True)
                continue

            if command == "ROLL":
                # 주사위 굴리기 결과 받기
                str_a, str_b = args
                for i, c in enumerate(str_a):
                    dice_a[i] = int(c)  # 문자를 숫자로 변환
                for i, c in enumerate(str_b):
                    dice_b[i] = int(c)  # 문자를 숫자로 변환
                my_bid = game.calculate_bid(dice_a, dice_b)
                print(f"BID {my_bid.group} {my_bid.amount}", flush=True)
                continue

            if command == "GET":
                # 주사위 받기
                get_group, opp_group, opp_score = args
                opp_score = int(opp_score)
                game.update_get(
                    dice_a, dice_b, my_bid, Bid(opp_group, opp_score), get_group
                )
                continue

            if command == "SCORE":
                # 주사위 골라서 배치하기
                put = game.calculate_put()
                game.update_put(put)
                assert put.rule is not None
                print(f"PUT {put.rule.name} {''.join(map(str, put.dice))}", flush=True)
                continue

            if command == "SET":
                # 상대의 주사위 배치
                rule, str_dice = args
                dice = [int(c) for c in str_dice]
                game.update_set(DicePut(DiceRule[rule], dice))
                continue

            if command == "FINISH":
                # 게임 종료
                break

            # 알 수 없는 명령어 처리
            print(f"Invalid command: {command}", file=sys.stderr, flush=True)
            sys.exit(1)

        except EOFError:
            break


if __name__ == "__main__":
    main()
