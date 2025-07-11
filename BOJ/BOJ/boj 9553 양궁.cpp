#include <iostream>
#include <cmath>
#include <iomanip>


using namespace std;

typedef long double ld;

int T,N;


ld PI;
ld PI2;
ld dot(ld x, ld y, ld a, ld b){
    return (x * a) + (y * b);
}

ld vsize(ld x, ld y){
    return sqrt((x*x) + (y*y));
}

void solve(){
    cin >> N;
    ld ans = 0;
    double diff;
    for(int i = 0; i < N; i++){
        int X,Y,A,B;
        
        cin >> X >> Y;
        cin >> A >> B;
        ld ratio = dot(X,Y,A,B) / (vsize(X,Y) * vsize(A,B));
        if(ratio < -1) ratio = -1;
        if(ratio > 1) ratio = 1;
        diff = acos(ratio);
        ans += (diff / (PI2));
    }
    cout << fixed << setprecision(5);
    cout << ans << "\n";
}


int main(){
    PI = atan(1) * 4;
    PI2 = PI * 2;
    cin >> T;
    for(int i = 0; i < T; i++){
        solve();
    }
}