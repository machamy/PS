#include <iostream>


using namespace std;


int N;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    while(true){
        int num;
        cin >> num;
        if(num == 0) break;
        if(num % N){
            cout << num << " is NOT a multiple of " << N << ".\n";
        }else{
            cout << num << " is a multiple of " << N << ".\n";
        }
    }

    return 0;
}