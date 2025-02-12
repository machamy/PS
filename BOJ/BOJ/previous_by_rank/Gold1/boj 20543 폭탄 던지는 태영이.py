import sys
input = sys.stdin.readline
##################################################
# 문제를 푸는데 필요한 데이터만 남기는 작업
def Set_need_data(list_):
    new_list = [[0 for _ in range(n-m+1)] for _ in range(n-m+1)]

    for i in range(n-m+1):
        for j in range(n-m+1):
            # 양수만 남기기 위해 -값을 저장
            new_list[i][j] = -list_[i][j]

    return new_list

##################################################
n, m = map(int,input().split())

input_data = [list(map(int, input().split())) for _ in range(n)]

input_data = Set_need_data(input_data)

# 누적합이 저장될 2차원 배열
sum_ = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 정답이 저장될 배열 각 변의 0은 제외하고 폭탄 존재 가능한 영역만 남겼다.
answer = [[0 for _ in range(n-m+1)] for _ in range(n-m+1)]

# 값을 구하고 누적합을 갱신함
for i in range(n-m+1):
    for j in range(n-m+1):
        answer[i][j] = input_data[i][j] - sum_[i][j] + sum_[i+m][j] + sum_[i][j+m] - sum_[i+m-1][j+m] - sum_[i+m][j+m-1] + sum_[i+m-1][j+m-1]
        print((i,j))
        for k in range(n-m+1):
            print(" ".join(map(str, sum_[k][1:])))
        sum_[i+m][j+m] = sum_[i+m-1][j+m] + sum_[i+m][j+m-1] - sum_[i+m-1][j+m-1] + answer[i][j]

# 정답 출력
for i in range(m//2):
    print("0 "*n)

for i in range(n-m+1):
    print(" ".join(map(str, sum_[i][1:])))

for i in range(m//2):
    print("0 "*n)
    
print("--"*4)

# 정답 출력
for i in range(m//2):
    print("0 "*n)

for i in range(n-m+1):
    print("0 "*(m//2) + " ".join(map(str, answer[i])) + " 0"*(m//2))

for i in range(m//2):
    print("0 "*n)