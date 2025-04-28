#include <iostream>

#define MAX_N 100'000

using namespace std;
int N;
int A[MAX_N + 10];
int min_num = MAX_N + 1;
int max_num = 0;
int remain;
bool is_ok(){
    // 먼저 min -> max, max -> min +1
    // if(N % 2 == 1){
    //     return false;
    // }
    
    for(int i = min_num; i <= max_num; i++){
        if(A[i]){
           A[i]--;
           remain--;
        }else{
            return false;
        }
    }
    for(int i = min_num+1; i < max_num; i++){
        if(A[i]){
            A[i]--;
            remain--;
        }else{
            return false;
        }
    }
    for(int i = min_num; i < max_num; i++){
        if(A[i] == 0){
            continue;
        }
        if(A[i] > A[i+1]){
            return false;
        }
        A[i+1] -= A[i];
        remain -= A[i] * 2;
    }
    return remain == 0;
}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    cin >> N;
    remain = N;
    for(int i = 0; i < N; i++){
        int in;
        cin >> in;
        A[in]++;
        min_num = min(min_num, in);
        max_num = max(max_num, in);
    }

    if(is_ok()){
        cout << 1 << "\n";
    }else{
        cout << -1 << "\n";
    }

    return 0;
}