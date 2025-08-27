from collections import deque
import sys


N, M = map(int,input().split())

'''

카드더미
- left : 상단
- right : 하단

'''

class Player:

    def __init__(self):
        self.deck = deque()
        self.ground = deque()

    def top_ground(self):
        if self.ground:
            return self.ground[0]
        return None
    
    def pop_deck(self):
        if self.deck:
            return self.deck.popleft()
        return None
    
    def push_ground(self, card):
        self.ground.appendleft(card)

def move_ground_to_deck(ground : deque, deck : deque):
    while ground:
        # 그라운드의 오른쪽 카드를 덱의 오른쪽에 넣기
        card = ground.pop()
        deck.append(card)

# 전역
dodo = Player()
suyeon = Player()


# 초기 입력
for _ in range(N):
    d,s = map(int,input().split())
    # 밑에서부터 입력받음
    dodo.deck.appendleft(d)
    suyeon.deck.appendleft(s)


def print_state():
    print(f"---- {M} ----")
    print("Dodo's deck:", list(dodo.deck))
    print("Dodo's ground:", list(dodo.ground))
    print("Suyeon's deck:", list(suyeon.deck))
    print("Suyeon's ground:", list(suyeon.ground))
    print("-" * 30)
    pass

print_state = lambda : None

print_state()


def round():
    global dodo, suyeon, M

    dodo_card = dodo.pop_deck()
    if dodo_card is None or not dodo.deck:
        return True
    dodo.push_ground(dodo_card)

    print_state()

    if dodo.top_ground() == 5:
        move_ground_to_deck(suyeon.ground, dodo.deck)
        move_ground_to_deck(dodo.ground, dodo.deck)
    if (dodo.top_ground() is not None and suyeon.top_ground() is not None) and dodo.top_ground() + suyeon.top_ground() == 5:
        move_ground_to_deck(dodo.ground, suyeon.deck)
        move_ground_to_deck(suyeon.ground, suyeon.deck)
    M -= 1
    if M == 0:
        return True
    if not dodo.deck or not suyeon.deck:
        return True

    suyeon_card = suyeon.pop_deck()
    if suyeon_card is None or not suyeon.deck:
        return True
    suyeon.push_ground(suyeon_card)

    print_state()

    if suyeon.top_ground() == 5:
        move_ground_to_deck(suyeon.ground, dodo.deck)
        move_ground_to_deck(dodo.ground, dodo.deck)
    if (dodo.top_ground() is not None and suyeon.top_ground() is not None) and dodo.top_ground() + suyeon.top_ground() == 5:
        move_ground_to_deck(dodo.ground, suyeon.deck)
        move_ground_to_deck(suyeon.ground, suyeon.deck)
    M -= 1
    if M == 0:
        return True
    if not dodo.deck or not suyeon.deck:
        return True
    
    print_state()


    return False


    


while M:
    brk = round()
    if brk:
        break

print_state()

if len(dodo.deck) == len(suyeon.deck):
    print("dosu")
elif len(dodo.deck) > len(suyeon.deck):
    print("do")
else:
    print("su")