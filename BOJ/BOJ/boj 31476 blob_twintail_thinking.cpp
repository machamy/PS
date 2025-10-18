#include <iostream>

using namespace std;

int D,N,U,T;

bool broken[1 << 12 + 1][1 << 12 + 1];

int twintail(int depth, int room, int t, int cost = 0){
    // cout << "twin depth : " << depth << " room : " << room << " cost : " << cost << "\n";
    if(depth == D - 1) return cost;
    int left = -1, right = -1;
    bool leftPossible = !broken[room][room*2];
    bool rightPossible = !broken[room][room*2+1];
    int nextT = t + (leftPossible && rightPossible ? T : 0);
    if(leftPossible == false && rightPossible == false){
        return cost;
    }
    if(leftPossible){
        left = twintail(depth + 1, room * 2,nextT, cost + U + nextT);
    }
    if(rightPossible){
        right = twintail(depth + 1, room * 2 + 1,nextT, cost + U + nextT);
    }
    int res = -1;
    res = max(left, right);

    return res;
}

int ponytail(int depth, int room, bool haveToReturn){
    // cout << "pony depth : " << depth << " room : " << room << " haveToReturn : " << haveToReturn << "\n";
    if(depth == D - 1){
        if(haveToReturn) return 2;
        else return 1;
    }
    
    int res = 1;
    int left = -1, right = -1;
    bool leftPossible = !broken[room][room*2];
    bool rightPossible = !broken[room][room*2+1];
    if(leftPossible){
        left = ponytail(depth + 1, room * 2, rightPossible || haveToReturn);
    }
    // cout << "room : " << room << " left : " << left << "\n";
    if(rightPossible){
        right = ponytail(depth + 1, room * 2 + 1, haveToReturn);
    }
    // cout << "room : " << room << " right : " << right << "\n";

    if(left > -1) res += left;
    if(right > -1) res += right;

    if(haveToReturn){
        res += 1;
    }

    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> D >> N >> U >> T;

    for(int i = 0; i < N; i++){
        int a,b;
        cin >> a >> b;
        broken[a][b] = true;
    }

    int twin = twintail(0,1,0);
    int pony = (ponytail(0,1,false) - 1) * U;
    // cout << twin << " " << pony << "\n";

    if(twin == pony) cout << ":blob_twintail_thinking:";
    else if(twin < pony) cout << ":blob_twintail_aww:";
    else cout << ":blob_twintail_sad:";
    return 0;
}