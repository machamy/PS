#include <iostream>

using namespace std;


int N;
int cnt[1001];

int calc(int startDepth);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N;
    for(int i = 1; i <= N; i++){
        cin >> cnt[i];
    }

    /*
    그냥 마지막 1이 아닐때까지 늘려나가면 되는거 아닌가???
    아니네... 루트 경유 안하는게 이득일수도
    1 2 2 2
    이러면 루트 경유 안하는게 이득!
    각 노드에 대해서 최대값을 찾은다음 그걸로 갱신하자
    
    .... 근데 여기서도 맞왜틀????
    어떤 경우가 있지...
    1, 2 말고 3이상이 의미가 있나??


    0 1 2 2 1 3 3 3 3 3 3

    */

    int ans = 0;
    for(int i = 0; i < N; i++){
        int temp = calc(i);
        // cout << "i : " << i << " temp : " << temp << "\n";
        ans = max(ans, temp);
    }
    cout << ans << "\n";
    
    return 0;
}

int calc(int startDepth){
    int A = N - startDepth;
    for(int depth = 1;  startDepth + depth <= N; depth++){
        if(cnt[startDepth + depth] <= 1){
            A = depth - 1;
            break;
        }
    }
    // cout << "A : " << A << "\n";
    // cout << "N - startDepth : " << N - startDepth << "\n";
    return A + (N - startDepth);
}