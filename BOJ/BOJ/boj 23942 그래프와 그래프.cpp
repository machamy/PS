#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int A,B,C;

vector<int> edges[11];
int ten = 10;
int main(){
    cin >> A >> B >> C;
// By = C - Ax
    if(B)
        for(int i = 1; i <= ten; i++){
            int val = (C - (double)A * i);
            if(val % B == 0){
                int y = val / B;
                if(y > 0 && y <= 10){
                    edges[i].push_back(y);
                }
            }
        }
    else{
        // Ax = C
        // x = C/A
        int val = C / A; // X값
        if(C % A == 0 && val > 0 && val <= 10){
            for(int i = 1; i <= ten; i++){
                    edges[val].push_back(i);
            }
        }
    }
    

    for(int i = 1; i <= ten; i ++){
        if(edges[i].empty()){
            cout << 0 << endl;
            continue;
         }
        sort(edges[i].begin(),edges[i].end());
        for(int e : edges[i]){
            cout << e << " ";
        }
        cout << endl;
    }
    return 0;
}