#include <iostream>
#include <tuple>
#include <utility>
#include <vector>
#include <algorithm>


using namespace std;
using pii = pair<int, int>;

int N,M;

bool hasToGroup[3001];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N >> M;

    // 일반도로
    for(int i = 0; i < M; i++){
        int s,e;
        cin >> s >> e;
        if(s < e){
            continue;
        }
        // e부터 s까지는 하나의 그룹이어야만함.
        for(int i = e+1; i <= s; i++){
            hasToGroup[i] = true;
        }
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


    
    */
    
    int currentSize;
    for(currentSize = 1; currentSize <= N; currentSize++){
        if(N % currentSize){
            continue;
        }
        bool isOk = true;
        for(int i = 1; i <= N; i += currentSize){
            if(hasToGroup[i]){
                isOk = false;
                break;
            }
        }
        if(isOk){
            // cout << "fail : " << currentSize << endl;
            break;
        }
    }
    cout << N / currentSize << endl;
    return 0;
}
