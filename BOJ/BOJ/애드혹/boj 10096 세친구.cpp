#include <iostream>
#include <vector>


using namespace std;

int N;
string U;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N >> U;
    int cnt = 0;
    if(!(N & 1)){
        cout << "NOT POSSIBLE" << endl;
        return 0;
    }

    vector<int> candidates;

    /*
        불가능한 경우의 수:
        1. N이 짝수인 경우 -> S 두개에 문자열 추가 아님 
        2. U가 S 두개가 아닌 경우

        가능한 경우의 수:
        1. 앞 S에 추가 
            - 앞 S가 끝나는 지점이 N/2
            - 뒤 S 시작 지점은 N/2 + 1
        2. 뒤 S에 추가
            - 앞 S가 끝나는 지점이 N/2 - 1
            - 뒤 S 시작 지점은 N/2

        N/2에 추가되어있는 경우는 따로 체크
        
    */
     
    // 앞 S 체크
    int i, j;
    int diffIdx = -1;
    int frontInfo = 1; // 0 : 불가능, 1 : 가능, 2 : 여러개 가능
    for(i = 0, j = N / 2 + 1; i <= N / 2; i++, j++){
        // cout << "i: " << i << ", j: " << j << endl;
        if(U[i] == U[j]){
            continue;
        }
        // cout << "U[i]: " << U[i] << ", U[j]: " << U[j] << endl;
        if(diffIdx == -1){
            diffIdx = i;
            i++;
            if(U[i] == U[j]){
                // cout << "continue" << endl;
                continue;
            } else {
                // cout << "diffIdx: " << diffIdx << endl;
                frontInfo = 0;
                break;
            }
        } else {
            frontInfo = 0; 
            break;
        }
    }

    // 뒤 S 체크
    diffIdx = -1;
    int backInfo = 1; // 0 : 불가능, 1 : 가능, 2 : 여러개 가능
    for(i = 0, j = N / 2; i < N / 2; i++, j++){
        if(U[i] == U[j]){
            continue;
        }
        if(diffIdx == -1){
            diffIdx = i;
            j++;
            if(U[i] == U[j]){
                continue;
            } else {
                backInfo = 0;
                break;
            }
        } else {
            backInfo = 0; 
            break;
        }
    }
    // cout << "frontInfo: " << frontInfo << ", backInfo: " << backInfo << endl;

    if(frontInfo && backInfo){
        cout << "NOT UNIQUE" << endl;
        return 0;
    }

    if(frontInfo == -1 && backInfo == -1){
        cout << "NOT POSSIBLE" << endl;
        return 0;
    }
    if(frontInfo == 0 && backInfo == 0){
        cout << "NOT POSSIBLE" << endl;
        return 0;
    }

    if(frontInfo){
        for(i = N /2 + 1; i < N; i++){
            cout << U[i];
        }
        cout << endl;
    }

    if(backInfo){
        for(i = 0; i < N / 2; i++){
            cout << U[i];
        }
        cout << endl;
    }


    return 0;
}