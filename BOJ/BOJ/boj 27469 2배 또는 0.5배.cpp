#include <iostream>

using namespace std;

int N;
/*
이전 증가량이 다음 증가량의 2배 혹은 0.5배

홀수일때

N = 6
1 2 4 3 5 6 8 7

N = 7
1 2 4 3 5 6

N = 8
1 3 2 4 5 7 6 8

*/

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    cout << "YES\n";
    if(N % 4 == 2){
        for(int i = 1; i <= N; i++){
            switch(i % 4){
                case 1:
                    cout << i << " ";
                    break;
                case 2:
                    cout << i << " ";
                    break;
                case 3:
                    cout << i + 1 << " ";
                    break;
                case 0:
                    cout << i - 1 << " ";
                    break;
            }
        }

    }else{
        for(int i = 1; i <= N; i++){
            switch(i % 4){
                case 1:
                    cout << i << " ";
                    break;
                case 2:
                    cout << i + 1 << " ";
                    break;
                case 3:
                    cout << i - 1 << " ";
                    break;
                case 0:
                    cout << i << " ";
                    break;
            }
        }
    }

    cout << "\n";

    return 0;
}