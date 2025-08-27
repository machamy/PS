#include <iostream>
#include <list>

using namespace std;

using pii = pair<int, int>;

int main(){
    int N;

    cin >> N;
    list<pii> l;
    for(int i = 1; i <= N; i++){
        int x;
        cin >> x;
        l.push_back({x, i});
    }
    auto cur = l.begin();
    int remainMove = 0;
    while(l.size()> 1){
        while(remainMove){
            if(remainMove < 0){
                if(cur == l.begin()){
                    cur = l.end();
                }
                cur--;
                remainMove++;
            } else {
                cur++;
                remainMove--;
                if(cur == l.end()){
                    cur = l.begin();
                }
            }
        }
        remainMove = (*cur).first;
        cout << (*cur).second << ' ';
        // cout << (*cur).first << ", " << (*cur).second << endl;
        auto eraseIt = cur;
        if(remainMove < 0){
            remainMove++;
            if(cur == l.begin()){
                cur = l.end();
            }
            cur--;
        } else {
            remainMove--;
            cur++;
            if(cur == l.end()){
                cur = l.begin();
            }
        }
        l.erase(eraseIt);
    }
    cout << (*l.begin()).second;
    cout << endl;
    return 0;
}