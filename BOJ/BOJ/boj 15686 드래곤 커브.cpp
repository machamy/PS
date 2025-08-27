#include <iostream>
#include <vector>
using namespace std;

struct Curve {
    int x, y, d, g;
};

// 방향: 0:우, 1:상, 2:좌, 3:하
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};

bool edges[101][101] = {false};
Curve curves[21];
vector<int> curve_info;

// 시계방향 회전
int cw(int d) {
    return (d + 1) % 4;
}

// 세대별 방향 정보 생성
void init_info(int d, int g) {
    curve_info.clear();
    curve_info.push_back(d);

    for (int gen = 1; gen <= g; gen++) {
        int size = curve_info.size();
        for (int i = size - 1; i >= 0; i--) {
            curve_info.push_back(cw(curve_info[i]));
        }
    }
}

// 커브 그리기
void draw_curve(int x, int y, int d, int g) {
    init_info(d, g);
    edges[x][y] = true;

    for (int i = 0; i < curve_info.size(); i++) {
        x += dx[curve_info[i]];
        y += dy[curve_info[i]];
        if (x >= 0 && x <= 100 && y >= 0 && y <= 100)
            edges[x][y] = true;
    }
}

// 정사각형 확인
bool is_square(int x, int y) {
    return edges[x][y] && edges[x + 1][y] &&
           edges[x][y + 1] && edges[x + 1][y + 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int x, y, d, g;
        cin >> x >> y >> d >> g;
        draw_curve(x, y, d, g);
    }

    int ans = 0;
    for (int x = 0; x < 100; x++) {
        for (int y = 0; y < 100; y++) {
            if (is_square(x, y)) ans++;
        }
    }

    cout << ans << '\n';
    return 0;
}
