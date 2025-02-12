#include <cstdio>
#include <algorithm>

using namespace std;

int dp[10004][11], n;
char from[10004];
char to[10004];

int dpf(int k, int turn) {
    int &ret = dp[k][turn];
    if (ret) return ret;
    if (k == n) return 0;
    int turnLeft = (to[k] - from[k] - turn + 20) % 10;
    int turnRight = 10 - turnLeft;
    return ret = min(dpf(k + 1, (turn + turnLeft) % 10) + turnLeft, dpf(k + 1, turn) + turnRight);
}

int main() {
    scanf("%d", &n);
    scanf("%s %s", from, to);
    for (int i = 0; i < n; i++) {
        from[i] -= '0';
        to[i] -= '0';
    }
    printf("%d", dpf(0, 0));
}