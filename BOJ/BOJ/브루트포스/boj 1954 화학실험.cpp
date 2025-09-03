#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*

n가지 종류의 시약과 M의 용액

*/

struct Reagent{
    int id;
    int a;
    int b;

    int gas(int x){
        return a * x + b;
    }

    bool check(int target,int& used){
        // target = a * x + b
        // x = (target - b) / a
        int tmp = target - b;
        if (tmp % a != 0) return false;
        int x = tmp / a;
        used += x;
        return true;
    }
};

int N;
Reagent reagents[100];
int M;
int MAX = 0;
int MIN = 10000 * 100 + 1000 + 1;

bool check(int target);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
 
    cin >> N;
    for (int i = 0; i < N; i++) {
        reagents[i].id = i;
        cin >> reagents[i].a >> reagents[i].b;
        int gas = reagents[i].gas(M);
    }

    cin >> M;

    for (int i = 0; i < N; i++) {
        int gas = reagents[i].gas(M);
        MAX = max(MAX, gas);
        MIN = min(MIN, reagents[i].b);
    }

    for(int target = MIN; target <= MAX; target++) {
        if (check(target)) {
            cout << target << "\n";
            return 0;
        }
    }
    cout << 0 << endl;

    return 0;
}

bool check(int target){
    int remain = M;
    // cout << "Checking target: " << target << "\n";
    for (int i = 0; i < N; i++) {
        int used = 0;
        // cout << "Reagent " << i << ": ";
        if (!reagents[i].check(target, used)) {
            // cout << "Failed at reagent " << i << "\n";
            return false;
        }
        // cout << "Used " << used << " of reagent " << i << "\n";
        remain -= used;
        if (remain < 0) {
            // cout << "Used too much reagent at " << i << "\n";
            return false;
        }
    }
    if (remain != 0) {
        // cout << "Not enough reagent used, remain: " << remain << "\n";
        return false;
    }
    return true;
}
