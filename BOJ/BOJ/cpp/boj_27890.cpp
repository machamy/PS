#include <iostream>

using namespace std;

int x,N;


int main(void){
    cin >> x >> N;

    for(int i = 0; i < N; i++){
        if (x&1){
            x=(2*x)^6;
        }else{
            x=(x/2)^6;
        }
    }
    cout << x << endl;
    return 0;
}