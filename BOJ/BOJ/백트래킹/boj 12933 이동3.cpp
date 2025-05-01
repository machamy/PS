#include <iostream>
#include <algorithm>

using namespace std;

int X,Y;
bool flag = false;
int go(int x, int y, int level){
    if(flag) return 1;
    if(x == X && y == Y){
        flag = true;
        return 1;
    }
    int res = 0;
    
    
    if(x + level <= X){
        res = max(res, go(x + level, y, level * 3));
    }
    if(y + level <= Y){
        res = max(res, go(x, y + level, level * 3));
    }
    return res;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> X >> Y;
    int res = go(0, 0, 1);
    cout << res << "\n";
    return 0;
}