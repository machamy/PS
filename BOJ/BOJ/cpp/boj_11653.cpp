#include <iostream>
#include <algorithm>

using namespace std;

int N;


int main(void){
    int current;
    cin >> N;

    current = 2;
    while (N != 1){
        if (N%current==0){
            cout << current << endl;
            N /= current;
        }else{
            current++;
        }
    }

    cout << left << endl;

    return 0;
}