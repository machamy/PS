#include <iostream>

using namespace std;

int N,K;
string S;

char leftChar(int n) {
    int idx = n - 1;
    if (idx < 0) idx += N;
    return S[idx];
}
char rightChar(int n) {
    int idx = (n + 1) % N;
    return S[idx];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    
    cin >> N >> K;
    cin >> S;

    while(K--) {
        string newS = S;
        for (int i = 0; i < N; i++) {
            char L = leftChar(i);
            char P = S[i];
            char R = rightChar(i);
            if((L == P && P == R) || (L != P && P != R && L != R)) {
                // 모두 같거나 모두 다르면 파랑으로
                newS[i] = 'B';
            } else{
                int cntR = (R == 'R') + (P == 'R') + (L == 'R');
                int cntG = (R == 'G') + (P == 'G') + (L == 'G');
                int cntB = (R == 'B') + (P == 'B') + (L == 'B');
                if(cntR == 2 && cntG == 1) newS[i] = 'R';
                else if(cntG == 2 && cntB == 1) newS[i] = 'R';
                else if(cntB == 2 && cntR == 1) newS[i] = 'R';
                else{
                    newS[i] = 'G';
                }
            }
        }
        S = newS;
    }

    int cntR = 0, cntG = 0, cntB = 0;
    for(char c : S) {
        if(c == 'R') cntR++;
        else if(c == 'G') cntG++;
        else cntB++;
    }   
    cout << cntR << ' ' << cntG << ' ' << cntB << '\n';

    return 0;
}