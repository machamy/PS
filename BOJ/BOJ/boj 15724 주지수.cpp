#include <iostream>

using namespace std;

int N,M;

int K;

int area[1024][1024];
int prefix[1024][1024];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin >> area[i][j];
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            prefix[i][j] = area[i][j];
            if(i > 0) prefix[i][j] += prefix[i-1][j];
            if(j > 0) prefix[i][j] += prefix[i][j-1];
            if(i > 0 && j > 0) prefix[i][j] -= prefix[i-1][j-1];
        }
    }

    cin >> K;
    for(int i = 0; i < K; i++){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        x1--; y1--; x2--; y2--;

        int sum = prefix[x2][y2];
        if(x1 > 0) sum -= prefix[x1-1][y2];
        if(y1 > 0) sum -= prefix[x2][y1-1];
        if(x1 > 0 && y1 > 0) sum += prefix[x1-1][y1-1];

        cout << sum << '\n';
    }
    

    return 0;
}