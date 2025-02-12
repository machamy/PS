#include <iostream>
#include <algorithm>

using namespace std;

int N,K;


int main(void){
    long long left,right,mid;

    cin >> N >> K;

    left = 1;
    right = K;
    while (left<right){
        int count = 0;
        mid = (left+right)/2;

        for(int i=1;i<=N;i++){
            count += (mid/i<N) ? mid/i : N;
        }

        if (count < K){
            left = mid+1;
        } else{
            right = mid;
        }
    }

    cout << left << endl;

    return 0;
}