#include <iostream>
#include <tuple>
#include <utility>
#include <vector>
#include <algorithm>


using namespace std;
using pii = pair<int, int>;

int N,M;

vector<int> adj[3001];
int minSize[3001] = {0,};
int minSizeGroupIds[3001] = {0,};


int getMinCity(int city);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N >> M;

    // 고속도로
    for(int i = 1; i < N; i++){
        adj[i].push_back(i + 1);
    }

    // 일반도로
    for(int i = 0; i < M; i++){
        int s,e;
        cin >> s >> e;
        if(adj[s].size() && adj[s][0] == e){
            continue;
        }
        adj[s].push_back(e);
    }

    for(int i = 1; i <= N; i++){
        sort(adj[i].begin(), adj[i].end());
    }

    /*
        지역을 나누어야함.
        1. 모든 지역은 도시의 수가 같아야함.
        2. A -> B가 가능하면, B -> A는 불가능해야함.
    
        ---

        지역의 수는 N의 약수.
        고속도로는 n-1에서 n으로 이동. 
        -> 지역에 포함된 도시는 연속되어야함.
           ex) A: 1, 3. B: 2, 4
               1 -> 2 2 -> 3 존재. A <-> B 가능

        ---
        1. 도시를 내림차순을 탐색한다.
        2. 자신의 가장 낮은 도시까지는 반드시 연결되어야만 함.
        3. 도시별 최소한의 지역 크기를 구한다.
        ---

        1. 먼저 N의 약수를 구한다
        2. 가장 큰 약수부터 순차적으로 탐색.
    
    */
    
    vector<int> sizes;
 

    for(int city = N; city >= 1; city--){
        if(minSizeGroupIds[city] != 0){
            continue;
        }
        int minCity = getMinCity(city);
        sizes.push_back(city - minCity + 1);
        #ifndef ONLINE_JUDGE
        cout << "City: " << city << ", Min City: " << minCity << endl;
        for(int i = 1; i <= N; i++){
            cout << minSizeGroupIds[i] << " ";
        }
        cout << endl;
        #endif
    }

    #ifndef ONLINE_JUDGE
    cout << "Sizes: ";
    for(int size : sizes){
        cout << size << " ";
    }
    cout << endl;
    #endif

    int maxSize = *max_element(sizes.begin(), sizes.end());


    // 이제 나온 최소 지역의 크기들로 각 지역의 수를 통일 시키자.
    vector<int> divisors;
    for(int i = 1; i * i <= N; i++){
        if(N % i == 0){
            if(i >= maxSize) {
                divisors.push_back(i);
            }
            if(i != N / i && N / i >= maxSize){
                divisors.push_back(N / i);
            }
        }
    }

}

// 해당 도시에서 갈 수 있는 가장 작은 도시
int getMinCity(int city){
    minSizeGroupIds[city] = city;
    if(adj[city].empty()){
        return city;
    }
    int res = adj[city][0];

    if(res > city){
        return city;
    }
    minSizeGroupIds[res] = city;
    vector<int> stack;
    stack.push_back(res);
    while(!stack.empty()){
        int cur = stack.back();
        stack.pop_back();
        res = min(res, cur);
        for(int next : adj[cur]){
            if(minSizeGroupIds[next] != city){
                stack.push_back(next);
                minSizeGroupIds[next] = city;
            }
        }
    }
    return res;
}