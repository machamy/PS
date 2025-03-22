#include <iostream>
#include <vector>

using namespace std;

int K;

/*
  2    3    4    5    6    7    8    9
  1    2    3    4    5    6    7    8    9   10  11 12  13  14
  0    1    2    3    4    5    6    7    8    9
010  011  100  101  110  111 1000 1001
001  010  011  100  101  110  111 1000 1001
000  001  010  011  100  101  110  111 1000
  0    1    0    1    2    3    
  4    7   44   47   74   77  444  447  474 477 744 747 774 777

2개 -> 4개 -> 8개 -> ...
*/

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    cin >> K;
    K += 1;
    vector<int> ans;
    while(true){
        int n = (K) % 2;
        ans.push_back((n == 1) ? 7 : 4);
        K /= 2;
        if(K == 0){
            break;
        }
    }
    ans.pop_back();
    while(!ans.empty()){
        cout << ans.back();
        ans.pop_back();
    }
    

    return 0;
}