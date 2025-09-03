#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int N;

int to_id(string s){
    if(s == "II") return 0;
    if(s == "NN") return 1;
    if(s == "UU") return 2;
    if(s == "IN" || s == "NI") return 3;
    if(s == "UN" || s == "NU") return 4;
    return 5; // IU, UI
}

int length[6] = {0};

int main() {

    cin >> N;

    for(int i = 0; i < N; i++) {
        string s;
        int len;
        cin >> s >> len;
        int id = to_id(s);
        length[id] += len;
    }
    int ans = 0;
    if((bool)length[3] + (bool)length[4] + (bool)length[5] >= 2) {
        // 모두 가능
        ans = length[0] + length[1] + length[2] + length[3] + length[4] + length[5];
    }
    else if(length[3]){
        // IN
        ans = max(length[0] + length[1] + length[3], length[2]);

    }else if(length[4]){
        // UN
        ans = max(length[1] + length[2] + length[4], length[0]);
    }
    else if(length[5]){
        // IU
        ans = max(length[0] + length[2] + length[5], length[1]);
    }
    else{
        // II, NN, UU
        ans = max({length[0], length[1], length[2]});
    }
    cout << ans << endl;
    return 0;
}

