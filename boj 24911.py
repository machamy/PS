emojitable = {
    'π’': '1234',
    'β­': '0',
    'π': '11',
    'πΎοΈ': '0',
    'π': '1',
    'π': '2',
    'π': '3',
    'π': '4',
    'πͺ': '24',
    'π±': '8',
    'π°': '777',
    'π': '17',
    'π': '17',
    'π': '17',
    'π': '18',
    'π―': '100',
    'π₯': '1', 'π₯': '2', 'π₯': '3',
    'π': '10',
    '0οΈβ£': '0',
    '1οΈβ£': '1',
    '2οΈβ£': '2',
    '3οΈβ£': '3',
    '4οΈβ£': '4',
    '5οΈβ£': '5',
    '6οΈβ£': '6',
    '7οΈβ£': '7',
    '8οΈβ£': '8',
    '9οΈβ£': '9',
    'π¨βπ«': '4',
    'π©βπ«': '4',
}
numtable = {
    '1234': 'π’',
    '100': 'π―',
    '10': 'π',
    '17': 'π',
    '0': '0οΈβ£',
    '1': '1οΈβ£',
    '2': '2οΈβ£',
    '3': '3οΈβ£',
    '4': '4οΈβ£',
    '5': '5οΈβ£',
    '6': '6οΈβ£',
    '7': '7οΈβ£',
    '8': '8οΈβ£',
    '9': '9οΈβ£',
}


def get_single_num(s: str):
    if s in emojitable:
        return emojitable[s]
    if s.endswith('βπ«'):
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
