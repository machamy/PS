#include <iostream>
#include <algorithm>


using namespace std;

int N;
int A[500'001];

int sort(){
    bool changed = false;
    for (int i=1; i<=N+1; i++) {
        changed = false;
        for (int j=1; j<=N-i; j++) {
            if (A[j] > A[j+1]) {
                changed = true;
                swap(A[j], A[j+1]);
            }
        }
        if (changed == false) {
            return i;
            break;
        }
    }
}
int main(void) {

    cin >> N;

    for (int i = 1; i <= N; i++) {
        cin >> A[i];
    }
    int cnt = sort();
    cout << cnt << "\n";
    return 0;
}