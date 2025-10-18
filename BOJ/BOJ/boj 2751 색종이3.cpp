#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

constexpr int MAX = 100;
constexpr int SIZE = 10;

int N;
int paper[MAX][MAX];

void printPaper(){
    for(int y = MAX - 1; y >= 0; y--){
        for(int x = 0; x < MAX; x++){
            if(paper[x][y] < 10) cout << ' ';
            cout << paper[x][y] << ' ';
        }
        cout << '\n';
    }
}

int getMax(int x, int y){

    int width = 1;
    int height = paper[x][y];
    int currentMax = height;
    for(; x + width < MAX; width++){
        if(paper[x + width][y] == 0) break;
        height = min(height, paper[x + width][y]);
        currentMax = max(currentMax, height * (width + 1));
    }

    return currentMax;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int _ = 0; _ < N; _++) {
        int x,y;
        cin >> x >> y;

        for(int dy = 0; dy < SIZE; dy++){
            for(int dx = 0; dx < SIZE; dx++){
                paper[x + dx][y + dy] = 1;
            }
        }
    }

    for(int y = 1; y < MAX; y++){
        for(int x = 0; x < MAX; x++){
            if(paper[x][y] == 0) continue;
            paper[x][y] += paper[x][y - 1];
        }
    }

    int ans = 0;
    for(int x = 0; x < MAX; x++){
        for(int y = 0; y < MAX; y++){
            if(paper[x][y] == 0) continue;
            ans = max(ans, getMax(x, y));
        }
    }

    // printPaper();
    cout << ans << '\n';

    return 0;

}