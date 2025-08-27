#include <iostream>


using namespace std;


int N, Q;
bool ans = false;
/*
1 2 3 4 5 6 7 8 9 10
1 2 6 4 5 3 7 8 9 10

*/

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> N >> Q;


    for (int i = 0; i < Q; i++) {
        int cmd, l, r;
        cin >> cmd >> l >> r;
        if(cmd == 1){
            ans = !ans;
        }
        else
        {
            int cnt =( r - l + 1) /2;
            if(cnt % 2 == 1){
                ans = !ans;
            }
        }

        cout << (int) ans << "\n";
    }

    return 0;

}