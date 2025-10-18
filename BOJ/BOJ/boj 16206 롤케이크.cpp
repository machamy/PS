#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

constexpr int TARGET = 10;

int N, M;
int A[1001];
int ans = 0;

// 10으로 나누어 떨어지는 것들을 우선순위, 더 작은것 우선순위
bool compare_func(int a, int b){
    if(a % TARGET == 0 && b % TARGET == 0){
        return a < b;
    } else if(a % TARGET == 0){
        return true;
    } else if(b % TARGET == 0){
        return false;
    } else {
        return a < b;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;

    vector<int> candidates;

    for(int i = 0; i < N; i++){
        cin >> A[i];
        if(A[i] == TARGET){
            ans++;
        }else if(A[i] < TARGET){
            continue;
        }else {
            candidates.push_back(A[i]);
        }
    }

    int cut_cnt = 0;
    sort(candidates.begin(), candidates.end(), compare_func);

    for(int i = 0; i < candidates.size(); i++){
        int val = candidates[i];
        
        while(val > TARGET && cut_cnt < M){
            val -= TARGET;
            cut_cnt++;
            ans++;
        }
        if(val == TARGET){
            ans++;
        }
    }
#if 0
    // 10으로 나누어 떨어지는 것들 우선 체크
    // 20 , 30 이 있을때 2번 자를 수 있으면 10/10, 10,20 이랑 20, 10/10/10 가능.
    // 가장 작은거부터 하면 ㅇㅋ
    sort(stack_ten.begin(), stack_ten.end());
    for(int i = 0; i < stack_ten.size(); i++){
        int val = stack_ten[i];
        int div = val / TARGET; // 20 이면 2, 자르는 횟수는 1
        if(cut_cnt + div - 1 <= M){
            ans += div;
            cut_cnt += div - 1;
        } else if(cut_cnt < M){
            ans += M - cut_cnt;
            cut_cnt = M;
            break;
        } else {
            break;
        }
    }


    // 안나누어 떨어지는 것들 체크

    for(int i = 0; i < stack.size(); i++){
        int val = stack[i];
        int div = val / TARGET; // 23 이면 2, 자르는 횟수는 2

        if(cut_cnt + div <= M){
            ans += div;
            cut_cnt += div;
        } else if(cut_cnt < M){
            ans += M - cut_cnt;
            cut_cnt = M;
            break;
        } else {
            break;
        }
    }
#endif

    cout << ans << '\n';

    return 0;
}