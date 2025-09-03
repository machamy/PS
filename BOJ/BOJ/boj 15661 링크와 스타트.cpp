#include <iostream>
#include <vector>
#include <bitset>

using namespace std;


int N;
int Data[21][21];

int go(int flagA, int flagB, int scoreA, int scoreB, int depth){

    // cout << "flagA: " << bitset<8>(flagA) << ", flagB: " << bitset<8>(flagB) << "\n";
    // cout << "scoreA: " << scoreA << ", scoreB: " << scoreB << "\n";
    // cout << "depth: " << depth << "\n";
    if(depth == N){
        return abs(scoreA - scoreB);
    }
    // int visited = flagA | flagB;
    int nxt_scoreA = scoreA;
    int nxt_scoreB = scoreB;
    for(int other = 0; other < depth; other++){
        if(flagA & (1 << other)){
            nxt_scoreA += Data[depth][other];
        }
        if(flagB & (1 << other)){
            nxt_scoreB += Data[depth][other];
        }
    }
    int left = go(flagA | (1 << depth), flagB, nxt_scoreA, scoreB, depth + 1);
    int right = go(flagA, flagB | (1 << depth), scoreA, nxt_scoreB, depth + 1);
    return min(left, right);
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            int value;
            cin >> value;

            Data[i][j] += value;
            Data[j][i] += value;
        }
    }
    int ans = go(1, 0, 0, 0, 1);
    cout << ans << "\n";
    return 0;
}