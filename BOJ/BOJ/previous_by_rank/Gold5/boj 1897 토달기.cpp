#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

void fastio(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}


int N;
string startWord;

string wordArr[1000];
bool visited[1000] = {0,};
vector<int> dictionary[81];

bool isPossible(string& origin, string& target){
    bool isAdded = false;
    for(int i = 0; i < origin.length(); i++){
        if(origin[i] == target[i] && !isAdded)
            continue;
        if(origin[i] == target[i+1])
            {
                isAdded = true;
                continue;
        }
        return false;
    }
    return true;
}

int main(){
    cin >> N >> startWord;
    int startIdx;
    for(int i = 0; i < N; i++){
        string word;
        cin >> word;
        wordArr[i] = word;
        dictionary[word.length()].push_back(i);
        if(word == startWord)
            startIdx = i;
    }

    queue<int> q;
    q.push(startIdx);
    int ans = startIdx;
    while(!q.empty()){
        int c = q.front();
        q.pop();
        if (wordArr[ans].length() < wordArr[c].length()){
            ans = c;
        }
        for(int nxt:dictionary[wordArr[c].length() + 1]){
            if(visited[nxt])
                continue;
            if(!isPossible(wordArr[c],wordArr[nxt]))
                continue;
            q.push(nxt);
            visited[nxt] = true;
        }
    }
    cout << wordArr[ans] << "\n";
}
