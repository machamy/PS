#include <iostream>
#include <queue>

using namespace std;

int N;
int hp[200'001];
int atk[200'001];

queue<int> alive;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        alive.push(i);
        cin >> atk[i];
    }
    for (int i = 0; i < N; i++)
    {
        cin >> hp[i];
    }
    int damage = 0; 
    // 최후의 1인까지 반복
    while(alive.size() > 1){
        int current = alive.front(); alive.pop();
        if(hp[current] <= damage){
            // 죽음
            continue;
        }
        hp[current] += atk[current];
        damage += atk[current];
        alive.push(current);
    }
    cout << alive.front() + 1<< endl;

    return 0;
}