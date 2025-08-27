#include <iostream>

using namespace std;

int N;
int arr[51];


int main(){
    cin >> N;
    for(int i = 0 ; i < N; i ++){
        cin >> arr[i];
    }

    bool flag = true;
    int cnt_double = 0;
    int cnt_plus = 0;
    while(flag){
        flag = false;
        for(int i = 0; i < N; i++){
            if(arr[i] % 2 == 1){
                cnt_plus++;
                arr[i]--;
            }
            if(arr[i]){
                arr[i] /= 2;
                flag = true;
                continue;
            }
        }
        if(flag){
            cnt_double++;
        }
    }
    cout << cnt_plus << endl << cnt_double << endl;
    cout << cnt_double + cnt_plus << endl;
}