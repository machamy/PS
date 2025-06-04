#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <queue>

#define MAX_AGE 1011

using namespace std;

int D8[8][2] = {
    {1,0}, {0,1}, {-1,0}, {0,-1},
    {1,1}, {-1,1}, {-1,-1}, {1,-1}
};

// struct MyTree{
//     int x,y;
//     int age;
// };

// struct cmp{
//     bool operator()(MyTree a, MyTree b){
//         return a.age > b.age;
//     }
// };

typedef pair<int,int> pii;

int N,M,K;
int year;
int A[11][11];
int norishment[11][11];
int toadd[11][11];
vector<pii> trees[MAX_AGE+1];
/** 
    1. 봄 : 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
    2. 여름 : 나무가 죽는다. 나무의 나이를 2로 나눈 나머지 만큼 양분이 된다.
    3. 가을 : 나무가 번식한다. 나무의 나이가 5의 배수일 때, 인접한 8방향에 나무가 생긴다.
    4. 겨울 : 땅에 양분을 추가한다.
*/
void yearCycle(){
    queue<pii> buffer;
    // cout << "year : " << year << endl;
    // 1. 봄 : 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
    for(int age = 1; age <= MAX_AGE; age++){
        int buff_size = buffer.size();
        while(trees[age].size())
        {
            pii tree = trees[age].back(); trees[age].pop_back();
            int r = tree.first;
            int c = tree.second;
            // cout << "age " << age << " r " << r << " c " << c;    
            if(norishment[r][c] < age){
                // 나무 죽음
                // cout << "  dead";
                toadd[r][c] += age / 2;
            }
            else{
                // 나무 삶
                // cout << "  alive"<< endl;
                norishment[r][c] -= age;
                // cout << norishment[r][c];
                buffer.push(tree);
            }
        }
        for(int i = 0; i < buff_size; i ++){
            trees[age].push_back(buffer.front());
            buffer.pop();
        }
    }

    // 2. 여름 : 죽은 나무가 양분으로 변한다
    for(int r = 1; r <= N; r++){
        for(int c = 1; c <= N; c++){
            norishment[r][c] += toadd[r][c];
            toadd[r][c] = 0;
        }
    }
    // 3. 가을 : 나무가 번식한다. 나무의 나이가 5의 배수일 때, 인접한 8방향에 나무가 생긴다.
    for(int age = 5; age <= MAX_AGE; age += 5){
        for(int i = 0; i < trees[age].size(); i++)
        {
            int r = trees[age][i].first;
            int c = trees[age][i].second;

            for(int dir = 0; dir < 8; dir++){
            int nr,nc;
            nr = r + D8[dir][0];
            nc = c + D8[dir][1];
            if(nr <= 0 || nr > N || nc <= 0 || nc > N)
                continue;
            trees[1].emplace_back(nr,nc);
            }
        }
    }

    // 4. 겨울 : 땅에 양분을 추가한다.
    for(int r = 1; r <= N; r++){
        for(int c = 1; c <= N; c++){
            norishment[r][c] += A[r][c];
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M >> K;

    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= N; j++){
            cin >> A[i][j];
            norishment[i][j] = 5;
        }
    }

    for(int i = 0; i < M; i++){
        int x,y,z;
        cin >> x >> y >> z;
        trees[z].emplace_back(x,y);
    }

    for(year = 1; year <= K; year++){
        yearCycle();
    }

    int ans = 0;
    for(int age = 1; age < MAX_AGE+1; age++){
        ans += trees[age].size();
    }
    // for(int r = 0; r < N; r++){
    //     for(int c = 0; c < N; c++){
    //         ans += trees[r][c].size();
    //     }
    // }
    cout << ans << "\n";
}


