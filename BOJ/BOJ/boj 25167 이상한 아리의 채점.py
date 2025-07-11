import sys

input = sys.stdin.readline

def time_to_min(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def solve():
    # N : 문제 수 M : 참가자 수 P : 제출 수
    N,M,P = map(int, input().split())
    participants = input().strip().split()
    participants.sort()  # 이름을 사전순으로 정렬
    name_to_index = {name: i for i, name in enumerate(participants)}
    scores = [0 for _ in range(M)]
    prev_wrong = [[-1 for _ in range(M)] for _ in range(N)] # 문제별, 사람의 이전 오답 시간
    times = [[float('inf') for _ in range(M)] for _ in range(N)] # 문제별, 사람의 정답 시간

    for _ in range(P):
        p, time_str, name, result = input().strip().split()
        p = int(p) - 1
        time = time_to_min(time_str)
        if times[p][name_to_index[name]] != float('inf'):
            # 이미 정답을 맞춘 문제는 무시
            continue
        if result == "solve":
            if prev_wrong[p][name_to_index[name]] == -1:
                # 부정행위!
                times[p][name_to_index[name]] = -100
            else:
                # 정답을 맞춘 경우
                # 이전 정답과의 시간 차이를 계산하고 저장
                times[p][name_to_index[name]] = time - prev_wrong[p][name_to_index[name]]
        else:
            # 오답인 경우
            if prev_wrong[p][name_to_index[name]] == -1:
                # 처음 오답인 경우
                prev_wrong[p][name_to_index[name]] = time

    
    for p in range(N): # 문제마다
        candidate_scores = []
        # print(f"Problem {p + 1}:")
        for i in range(M): # 참가자마다
            # print(participants[i], scores[i])
            if times[p][i] != float('inf'):
                # 정답을 맞춘 경우
                if times[p][i] == -100:
                    # 부정행위로 정답을 맞춘 경우
                    scores[i] += (M + 1)
                else:
                    # 정답인경우 순위 경쟁
                    candidate_scores.append((times[p][i], i))
            else:
                if prev_wrong[p][i] == -1:
                    # 제출 기록이 없는 경우
                    scores[i] += (M + 1)
                else:
                    # 오답만 있는 경우
                    scores[i] += (M)
        candidate_scores.sort()
        for i, e in enumerate(candidate_scores):
            time, person = e
            scores[person] += (i + 1)
        
        

    # 최종 순위 출력
    sorted_scores = sorted([(score, i) for i, score in enumerate(scores)])
    for score, idx in sorted_scores:
        print(participants[idx])
    
solve()