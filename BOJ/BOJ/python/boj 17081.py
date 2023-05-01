import sys

input = sys.stdin.readline

'''
 . 빈칸
 # 벽
 B 아이템상자
 
 ^ 가시 함정
 
 & 몬스터
 
 M 보스몬스터

'''
D4 = {
    'R': (0, 1),
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0)
}


class Entity:

    def __init__(self, i, j, max_health, attack, defense, exp):
        self.i = i
        self.j = j
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.defense = defense
        self.exp = exp


class Player(Entity):
    def __init__(self, i, j):
        self.lv = 1
        super().__init__(i, j, 20, 2, 2, 0)
        self.items = set()
        self.weapon = 0
        self.armor = 0

        self.fighting_monster = None

    def add_exp(self, amount):
        if 'EX' in self.items:
            amount *= 1.2
        self.exp += int(amount)
        if self.exp >= 5 * self.lv:
            self.lv_up()
            self.exp = 0

    def lv_up(self):
        self.lv += 1
        self.attack += 2
        self.defense += 2
        self.max_health += 5
        self.health = self.max_health

    def is_alive(self):
        return self.health > 0;

    def get_f_attack(self):
        return self.attack + self.weapon;

    def get_f_defense(self):
        return self.defense + self.armor;

    def add_item(self, item):
        if len(self.items) < 4:
            self.items.add(item)

    def fight(self, monster):
        self.fighting_monster = monster
        monster.health = monster.max_health
        buff = 1
        if "CO" in self.items:
            buff = 2
            if 'DX' in self.items:
                buff = 3
        while True:
            monster.health -= max(1, self.get_f_attack() * buff - monster.defense)
            buff = 1
            if monster.health <= 0:
                self.add_exp(monster.exp)
                if "HR" in self.items:
                    self.health = min(self.max_health, self.health + 3)
                board_info[monster.i][monster.j] = '.'
                return True
            if 'HU' in player.items and monster.boss:
                player.items.remove("HU")
                continue
            self.damage(max(1, monster.attack - self.get_f_defense()))
            if self.health <= 0:
                return False

    def damage(self, amount):
        self.health -= amount

    def move(self, ni, nj):
        board[self.i][self.j] = str(board_info[self.i][self.j])
        board[ni][nj] = '@'
        self.i = ni
        self.j = nj


class Monster(Entity):
    def __init__(self, i, j, name, max_health, attack, defense, exp):
        super().__init__(i, j, max_health, attack, defense, exp)
        self.i = i
        self.j = j
        self.name = name
        self.boss = False

    def __str__(self):
        return 'M' if self.boss else '&'


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
board_info = [list(board[i]) for i in range(N)]

monster_amount = 1
item_amount = 0

turns = 0

for l in board:
    monster_amount += l.count('&')
    item_amount += l.count('B')

p_i = p_j = 0
for i, l in enumerate(board):
    for j, e in enumerate(l):
        if e == '@':
            p_i = i
            p_j = j
            break
    else:
        continue
    break

cmds = input().rstrip()

# monster_list = [None for _ in range(monster_amount)]
# item_list = [None for _ in range(item_amount)]

for i in range(monster_amount):
    R, C, S, W, A, H, E = input().split()
    m = Monster(int(R) - 1, int(C) - 1, S, int(H), int(W), int(A), int(E))
    board_info[int(R) - 1][int(C) - 1] = m

for i in range(item_amount):
    R, C, T, S = input().split()
    if T in "WA":
        board_info[int(R) - 1][int(C) - 1] = (T, int(S))
    else:
        board_info[int(R) - 1][int(C) - 1] = (T, S)

player = Player(p_i, p_j)
board_info[p_i][p_j] = '.'
win = False
for cmd in cmds:

    turns += 1

    i, j = player.i, player.j
    ni, nj = i + D4[cmd][0], j + D4[cmd][1]
    if not (0 <= ni < N and 0 <= nj < M) or board[ni][nj] == '#':
        ni, nj = player.i, player.j
    if board[ni][nj] == 'B':
        T, S = board_info[ni][nj]
        if T == "W":
            player.weapon = S
        elif T == "A":
            player.armor = S
        else:
            player.add_item(S)
        board_info[ni][nj] = '.'
    elif board[ni][nj] == '^' or board_info[ni][nj] == '^':
        player.fighting_monster = Monster(ni, nj, "SPIKE TRAP", 0, 0, 0, 0)
        if 'DX' in player.items:
            player.damage(1)
        else:
            player.damage(5)
    elif board[ni][nj] in '&M':
        if board[ni][nj] == 'M':
            board_info[ni][nj].boss = True
            if "HU" in player.items:
                player.health = player.max_health

        res = player.fight(board_info[ni][nj])
        if res and board[ni][nj] == 'M':
            player.move(ni, nj)
            win = True
            break
        if res:
            board_info[ni][nj] = '.'

    if player.is_alive():
        player.move(ni, nj)
    else:
        if 'RE' in player.items:
            player.health = player.max_health
            player.move(p_i,p_j)
            player.items.remove("RE")
        else:
            board[player.i][player.j] = board_info[player.i][player.j]
            break

for l in board:
    print(''.join(l))
print(f"Passed Turns : {turns}")
print(f"LV : {player.lv}")
print(f"HP : {max(player.health, 0)}/{player.max_health}")
print(f"ATT : {player.attack}+{player.weapon}")
print(f"DEF : {player.defense}+{player.armor}")
print(f"EXP : {player.exp}/{player.lv * 5}")
if player.is_alive():
    if win:
        print("YOU WIN!")
    else:
        print("Press any key to continue.")
else:
    print(f"YOU HAVE BEEN KILLED BY {player.fighting_monster.name}..")
