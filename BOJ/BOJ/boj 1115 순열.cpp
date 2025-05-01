#include <iostream>


using namespace std;

int N;
int A[50];
bool visited[50];

int check(int i){
    if(visited[i]) return 0;
    visited[i] = true;
    check(A[i]);
    return 1;
}

int main(void){
    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    int cycle = 0;
    for(int i = 0; i < N; i++){
        cycle += check(i);
    }
    if(cycle == 1){
        cout << 0 << "\n";
    }else{
        cout << cycle << "\n";
    }
    return 0;
}