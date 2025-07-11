#include <stdio.h>

#define Max(a,b) ((a) > (b) ? (a) : (b))

// using namespace std;

int N;
int width[1001];
int height[1001];

int dp[1001][2]; // 0 : 가로 1 : 세로

int abs(int n){
    return n < 0 ? -n : n;
}

int main(){
    int i,j;
    int ans;
    
    scanf("%d",&N);

    for(i = 0; i < N; i ++){
        scanf("%d %d", &width[i], &height[i]);
    }

    dp[0][0] = width[0];
    dp[0][1] = height[0];

    printf("dp[0][0] = %d, dp[0][1] = %d\n", dp[0][0], dp[0][1]);
    for(i = 1; i < N; i++){
        dp[i][0] = Max(dp[i-1][0] + abs(height[i-1] - height[i]), dp[i-1][1] + abs(width[i-1] - height[i])) + width[i];
        dp[i][1] = Max(dp[i-1][0] + abs(height[i-1] - width[i]), dp[i-1][1] + abs(width[i-1] - width[i])) + height[i];

        printf("dp[%d][0] = %d, dp[%d][1] = %d\n", i, dp[i][0], i, dp[i][1]);
    }
    if(dp[N-1][0]> dp[N-1][1]) {
        ans = dp[N-1][0];
    } else {
        ans = dp[N-1][1];
    }

    printf("%d\n", ans);

    return 0;
}