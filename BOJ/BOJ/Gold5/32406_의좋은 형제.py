import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # def get_diff(A, B):
    #     a_end = A[-2:]
    #     b_end = B[-2:]
        
    #     for i in range(N-2):
    #         if A[i] > B[i]:
    #             a_end[-2] += B[i]
    #             b_end[-2] += A[i]
    #         else:
    #             a_end[-1] += B[i]
    #             b_end[-1] += A[i]
    
    #     a_end[-1] += b_end[-2]
    #     b_end[-1] += a_end[-2]
        
    #     return abs(a_end[-1] - b_end[-1])
    def get_diff2(A, B):
        a_end = A[-1]
        b_end = B[-1]
        
        for i in range(N-2):
            if A[i] > B[i]:
                a_end += A[i]
                b_end += B[i]
            else:
                a_end += B[i]
                b_end += A[i]
    
        a_end += B[-2]
        b_end += A[-2]
        
        return abs(a_end - b_end)
    
    print(max(get_diff2(A,B), get_diff2(B,A)))
    
   

solve()