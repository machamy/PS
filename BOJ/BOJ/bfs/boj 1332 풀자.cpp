#include <iostream>
#include <queue>
#include <tuple>
#include <utility>

using namespace std;

using pii = pair<int, int>;

struct Data{
    int checked; // 현재까지 체크한 문제
    int solved;  // 현재까지 푼 문제
    int min_val; // 현재까지 푼 문제의 최소값
    int max_val; // 현재까지 푼 문제의 최대값
};

int N, V;
int P[51];

int visited[51][51][2];// visited[checked][solved][0/1] -> 0: min, 1: max

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);


    cin >> N >> V;
    for(int i = 1; i <= N; i++){
        cin >> P[i];
    }

    for(int i = 0; i <= N; i++){
        for(int j = 0; j <= N; j++){
            visited[i][j][0] = 523123; // min
            visited[i][j][1] = -1; // max
        }
    }

    queue<Data> q;

    q.push({1, 1, P[1], P[1]});

    while(!q.empty()){
        auto [checked, solved, min_val, max_val] = q.front();
        q.pop();

        if(checked > N){
            continue;
        }
        if(max_val - min_val >= V){
            cout << solved  << endl;
            return 0;
        }

        for(int next = checked + 1; next <= checked + 2; next++){
            if(next > N) continue;
            int new_solved = solved + 1;
            int new_min = min(min_val, P[next]);
            int new_max = max(max_val, P[next]);

            if(visited[next][new_solved][0] > new_min ||
               visited[next][new_solved][1] < new_max) {
                visited[next][new_solved][0] = min(visited[next][new_solved][0], new_min);
                visited[next][new_solved][1] = max(visited[next][new_solved][1], new_max);
                q.push({next, new_solved, new_min, new_max});
            }
        }
    }


    cout << N << endl;

    return 0;
}