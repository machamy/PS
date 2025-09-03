#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N;
int N2;
int X[8];

int arr[17];

vector<vector<int>> results;

/*
dfs로 완전탐색 후 정렬
*/

bool dfs(int depth) {
    if(depth == N){
        results.push_back(vector<int>(arr, arr + N2));
        return true;
    }
    int n = X[depth];

    for(int i = 0; i < N2 - (n + 1); i++) {
        if(arr[i] == -1 && arr[i + n + 1] == -1){
            arr[i] = n;
            arr[i + n + 1] = n;
            if(dfs(depth + 1)) {
                ;
            }
            arr[i] = -1;
            arr[i + n + 1] = -1;
        }
    }
    return false;
}

int main(){
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> X[i];
    }
    N2 = N * 2;

    for(int i = 0; i < N2; i++) {
        arr[i] = -1;
    }

    sort(X, X + N);
    dfs(0);
    

    if(!results.empty()) {
        sort(results.begin(), results.end());
        vector<int>& result = results.front();
        for(int i = 0; i < N2; i++) {
            cout << result[i] << " ";
        }
        cout << endl;
    } else {
        cout << "-1" << endl;
    }

    return 0;
}