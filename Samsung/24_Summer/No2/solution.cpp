#define MAXL	5
#define MAXF	10
#define MAXN    10000

#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

unordered_set<int> friendData[MAXN+1];

void init(int N)
{
	for (int i = 0; i <= N; i++)
    {
       friendData[i].clear();
    }
}

void add(int id, int F, int ids[MAXF])
{
    for (size_t i = 0; i < F; i++)
    {
        friendData[id].insert(ids[i]);
        friendData[ids[i]].insert(id);
    }
}

void del(int id1, int id2)
{
    friendData[id1].erase(id2);
    friendData[id2].erase(id1);
}

int recommend(int id, int list[MAXL])
{
    unordered_map<int,long long> count;

    for (int friend_id : friendData[id]) {
        for (int ffriend : friendData[friend_id]) {
            if (ffriend != id && (friendData[id].find(ffriend) == friendData[id].end())) {
                count[ffriend]++;
            }
        }
    }

    vector<pair<int, long long>> result;
    for (const pair<int, long long> & entry : count) {
        result.push_back({entry.first, entry.second});
    }
    int recommend_num = result.size() < MAXL ? result.size() : MAXL;
    
    sort(result.begin(), result.end(), [](const pair<int, long long> &a, const pair<int, long long> &b) {
        if (a.second == b.second)
            return a.first < b.first;
        return a.second > b.second;
    });
    
    for(int i = 0; i<recommend_num; i++){
        list[i] = result[i].first;
    }
    

	return recommend_num;
}