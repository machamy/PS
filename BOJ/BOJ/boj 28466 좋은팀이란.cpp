#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <tuple>

using namespace std;

int N;
int cheongan[10][10];
int jeejee[12][12];

vector<int> skills[10][12];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            cin >> cheongan[i][j];
        }
    }

    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 12; j++) {
            cin >> jeejee[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        int score;
        string eeljoo;
        cin >> score >> eeljoo;
        int c = eeljoo[0] - '0'; // 천간
        int j = eeljoo[1] - 'A'; // 지지
        skills[c][j].push_back(score);
    }


    for (int c = 0; c < 10; c++) {
        for (int j = 0; j < 12; j++) {
            if (!skills[c][j].empty()) {
                sort(skills[c][j].begin(), skills[c][j].end());
            }
        }
    }

    int ans = 0;

   for(int i = 0; i < 120; i++) {
        int a_c = i / 12; // 천간
        int a_j = i % 12; // 지지
        if(skills[a_c][a_j].empty()) {
            continue;
        }
        int a_score = skills[a_c][a_j].back();
        skills[a_c][a_j].pop_back();
        for(int j = 0; j < 120; j++) {
            int b_c = j / 12;
            int b_j = j % 12;
            if(skills[b_c][b_j].empty()) {
                continue;
            }
            int b_score = skills[b_c][b_j].back();
            skills[b_c][b_j].pop_back();
            for(int k = 0; k < 120; k++) {
                int c_c = k / 12;
                int c_j = k % 12;
                if(skills[c_c][c_j].empty()) {
                    continue;
                }
                int c_score = skills[c_c][c_j].back();
                skills[c_c][c_j].pop_back();

                int score = a_score + b_score + c_score;
                score += cheongan[a_c][b_c] + cheongan[b_c][c_c] + cheongan[c_c][a_c];
                score += jeejee[a_j][b_j] + jeejee[b_j][c_j] + jeejee[c_j][a_j];
                ans = max(ans, score);
                skills[c_c][c_j].push_back(c_score);
            }
            skills[b_c][b_j].push_back(b_score);
        }
        skills[a_c][a_j].push_back(a_score);
    }

    cout << ans << '\n';

    return 0;
}