#include <iostream>

using namespace std;

int N,M,K;

/*
1 2 3 4
5 6 7 8
9 10 11 12


1 2 3 4 5
6 7 8 9 10
11 12 13 14 15


1 2
3 4




*/
int arr[1000][1000];
int main(){
    cin >> N >> M >> K;

    int n = 1;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            arr[i][j] = (i + 1) + j;
        }
    }

    if(arr[N-1][M-1] > K){
        cout << "NO" << endl;
        return 0;
    }
    cout << "YES" << endl;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}