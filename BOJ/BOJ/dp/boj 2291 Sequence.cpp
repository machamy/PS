#include <iostream>
#include <cstring>
#include <vector>

#define FASTIO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;
using ll = long long;

ll N,M,K;

// 현재번호, 숫자, sum
ll table[12][221][221];

// 현재번호, 이전숫자, 현재 합
ll dp(int idx, int num, int sum){
    if(idx > N || sum > M){
        return 0;
    }

    ll &ret = table[idx][num][sum];
    // cout << "dp "<<idx << ' ' << num << ' ' << sum << '\n';
    // cout << ret << '\n';
    if(ret != -1){
        return ret;
    }

    ret = 0;
    for(int i=num; i<=M; i++){
        ret += dp(idx+1,i,sum+i);
    }

    return ret;
}
void prettyPrintTable(){

    for(int i=1;i<=N;i++){
        cout << i << "번째\n";
        for(int j=1;j<=M;j++){
            for(int k=1;k<=M;k++){
                cout << table[i][j][k] << ' ';
            }
            cout << '\n';
        }
        cout << '\n';
    }
}

void printans(int idx, int num, int sum,ll K){
    if(idx > N){
        return;
    }

    for(int i = num; i<=M; i++){
        if(sum+i > M){
            break;
        }
        // cout << idx << ' ' << i << ' ' << sum << ' ' << K << '\n';
        // cout << table[idx+1][i][sum+i] << '\n';
        if(table[idx+1][i][sum+i] == -1){
            continue;
        }
        if(K <= table[idx+1][i][sum+i]){
            cout << i << ' ';
            printans(idx+1,i,sum+i,K);
            return;
        }else{
            K -= table[idx+1][i][sum+i];
        }
    }
    
}

int main(){
    FASTIO;

    cin >> N >> M >> K;

    memset(table,-1,sizeof(table));
    for(int i=1;i<=M;i++){
        table[N][i][M] = 1;
    }

    dp(0,1,0);
    // prettyPrintTable();
    for(int i=1;i<=K;i++){
        printans(0,1,0,i);
        cout << '\n';
    }
    
    cout << '\n';

}
