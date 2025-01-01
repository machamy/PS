#include <cmath>
#include <iostream>
#include <string.h>
#include <vector>

using namespace std;

int N;
bool visited[5001] = {false};
int res[5001];
bool flag = false;
#include <vector>

int dp[5001];

bool is_prime(int num) {
  if (num < 2)
    return false;
  if (dp[num] != -1)
    return dp[num];
  for (int i = 2; i <= sqrt(num); ++i) {
    if (num % i == 0) {
      dp[num] = 0;
      return false;
    }
  }
  dp[num] = 1;
  return true;
}

void dfs(int depth, int i, int total, int &res_size) {
  if (is_prime(total) || flag)
    return;
  if (depth == N) {
    cout << "YES" << endl;
    for (int k = 0; k < res_size; ++k) {
      cout << res[k] << " ";
    }
    cout << endl;
    flag = true;
    return;
  }
  for (int j = 1; j <= N; ++j) {
    if (!visited[j]) {
      visited[j] = true;
      res[res_size++] = j;
      dfs(depth + 1, j, total + j, res_size);
      visited[j] = false;
      --res_size;
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> N;

  memset(dp, -1, sizeof(dp));

  int res_size = 0;
  bool flag = false;
  for (int i = 1; i <= N; ++i) {
    visited[i] = true;
    res[res_size++] = i;
    dfs(1, i, i, res_size);
    visited[i] = false;
    --res_size;
    if (flag)
      break;
  }
  if (!flag) {
    cout << "NO" << endl;
  }

  return 0;
}