#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int N,M;
struct Group{
    string name;
    int amount;
    vector<string> members;
};

Group groups[101];


map<string,int> memberToGroup;
map<string,int> nameToGroup;

int main(){
    cin >> N >> M;
    for(int i = 0; i < N; i++){
        Group& g = groups[i];
        cin >> g.name;
        cin >> g.amount;
        nameToGroup[g.name] = i;
        for(int j = 0; j < g.amount; j++){
            string n;
            cin >> n;
            g.members.push_back(n);
            memberToGroup[n] = i;
        }
        sort(g.members.begin(),g.members.end());
    }

    for(int i =0; i<M;i++){
        int cmd;
        string str;
        cin >> str;
        cin >> cmd;
        
        // cout << cmd << ": " << str << endl;
        if(cmd == 0){
            // 해당 팀 멤버 전부
            Group& group = groups[nameToGroup[str]];
            for(int j = 0; j < group.amount; j++){
                cout << group.members[j] << "\n";
            }
        }else{
            Group& group = groups[memberToGroup[str]];
            cout << group.name << endl;
        }
    }
    return 0;
}