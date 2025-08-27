#include <iostream>
#include <vector>

using namespace std;

int N;

int main(){
    cin >> N;
    if(N == 3){
        cout << -1 << endl;
        return 0;
    } 
    int i = 1;
    for(; i < (N+1) /2; i++){
        cout << i + 1 << "\n";
    }
    cout << 1 << "\n";
    cout << N << "\n";
    i += 2;
    for(; i <= N; i++){
        cout << i-1 << "\n";
    }
    return 0;
}