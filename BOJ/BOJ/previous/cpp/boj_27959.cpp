#include <iostream>

using namespace std;

int N,M;

int main(void){
    cin >> N >> M;

    if (N*100 >= M){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
    return 0;
}