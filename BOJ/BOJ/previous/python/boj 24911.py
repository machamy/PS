emojitable = {
    '🔢': '1234',
    '⭕': '0',
    '🃏': '11',
    '🅾️': '0',
    '📕': '1',
    '📗': '2',
    '📘': '3',
    '📙': '4',
    '🏪': '24',
    '🎱': '8',
    '🎰': '777',
    '📅': '17',
    '📆': '17',
    '🗓': '17',
    '🔞': '18',
    '💯': '100',
    '🥇': '1', '🥈': '2', '🥉': '3',
    '🔟': '10',
    '0️⃣': '0',
    '1️⃣': '1',
    '2️⃣': '2',
    '3️⃣': '3',
    '4️⃣': '4',
    '5️⃣': '5',
    '6️⃣': '6',
    '7️⃣': '7',
    '8️⃣': '8',
    '9️⃣': '9',
    '👨‍🏫': '4',
    '👩‍🏫': '4',
}
numtable = {
    '1234': '🔢',
    '100': '💯',
    '10': '🔟',
    '17': '📆',
    '0': '0️⃣',
    '1': '1️⃣',
    '2': '2️⃣',
    '3': '3️⃣',
    '4': '4️⃣',
    '5': '5️⃣',
    '6': '6️⃣',
    '7': '7️⃣',
    '8': '8️⃣',
    '9': '9️⃣',
}


def get_single_num(s: str):
    if s in emojitable:
        return emojitable[s]
    if s.endswith('‍🏫'):
        return '4'


def get_num(s: str):
    result = []
    while s:
        for emoji in emojitable:
            if s.startswith(emoji):
                result.append(emojitable[emoji])
                s = s[len(emoji):]
    return "".join(result)


def get_emoji(n: int):
    num = str(n)
    result = []
    while num:
        for s in numtable:
            if num.startswith(s):
                result.append(numtable[s])
                num = num[len(s):]
        print(num)
    return "".join(result)


a = get_num(input())
b = get_num(input())
result = get_emoji(int(a) + int(b))
print(result)
# while True:
#     s = input()
#     #print(s,*[*map(ord,s)])
#
#     n = int(s)
#     x = getemoji(n)
#     y = int(getnum(x))
#     print(n,x,y)
#     print(n==y)
