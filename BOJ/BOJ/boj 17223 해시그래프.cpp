#include <iostream>
#include <vector>
#include <queue>

#define FASTIO ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

using namespace std;

struct CEvent{
    int time;
    int id;
    int from;
    int to;

    CEvent(int time, int id, int from, int to) : time(time), id(id), from(from), to(to) {};
};

int N, M;

vector<CEvent> recv_events[101];
// vector<CEvent> send_events[101];

void addEvent(int a, int b){
    static int time = -1;
    time++;
    CEvent e(time, recv_events[b].size(), a, b);
    recv_events[b].push_back(e);
    // if(a == b){
    //     return;
    // }
    // send_events[a].push_back(e);
    // return;
}

int findEvent(int a, int time){
    int l = 0, r = recv_events[a].size() - 1;
    vector<CEvent> &eventVector = recv_events[a]; // isRecv ? recv_events[a] : send_events[a];
    if(eventVector.empty()){
        return -1;
    }
    while(l < r){
        int mid = l + (r - l) / 2;
        if(eventVector[mid].time < time){
            l = mid + 1;
        }else{
            r = mid;
        }
    }
    return l;
}

int main(){
    // FASTIO;
    cin >> N >> M;
    
    for(int i = 0; i < N; i++){
        addEvent(i, i);
    }

    for(int i = 0; i < M; i++){
        int a, b;
        cin >> a >> b;
        addEvent(a, b);
    }
    int A,P,B,Q;
    cin >> A >> P >> B >> Q;
    queue<pair<int,int>> que;
    que.emplace(A, P);
    
    int visited[101]; // 해당 id까지는 방문했음.
    for(int i = 0; i < 101; i++){
        visited[i] = -1;
    }

    while(!que.empty()){
        auto [a, id] = que.front();
        que.pop();
        // cout << a << " " << id << "\n";
        // cout << "event : " << recv_events[a][id].id << " " << recv_events[a][id].from << " " << recv_events[a][id].to << "\n";
        // cout << "B " << B << " Q " << Q << endl;
        if(a == B){
            if(id >= Q){
                cout << 1 << "\n";
                return 0;
            }
            // cout << 0 << "\n";
            // return 0;
        }
        // if(id >= recv_events[a].size()){
        //     continue;
        // }
        CEvent &event = recv_events[a][id];
        int prntEventId = findEvent(event.from, event.time);
        prntEventId--;
        if(prntEventId < 0){
            prntEventId = 0;
        }
        if(visited[event.from] < prntEventId){
            // cout << "eventId " << eventId << "\n";
            que.emplace(event.from, prntEventId);
            
            // cout << "emplace : " << event.from << " " <<findEvent(event.from, event.time)<< "\n";
        }
        // cout << "visited[a] " << visited[a] << " id " << id << "\n";
        if(visited[a] < id){
            // queue.emplace(a, event.id);
            // cout << "id -1" << id - 1 << " visited[a] " << visited[a] << "\n";
            for(int i = id-1; i > visited[a]; i--){
                auto &event = recv_events[a][i];
                que.emplace(a, event.id);
                // cout << "emplace2 : " << event.to << " " << event.id << "\n";
            }
            visited[a] = event.id;
        }
    
    }
    cout << 0 << "\n";
    return 0;
}
