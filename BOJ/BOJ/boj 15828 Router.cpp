#include <iostream>
#include <queue>

using namespace std;

int N; // 버퍼 크기


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    queue<int> buffer;
    while(true){
        int packet;
        cin >> packet;
        if(packet == -1) break;
        if(packet == 0){
            // 패킷 하나 처리
            int processed = buffer.front();
            buffer.pop();
            continue;
        }
        // 패킷 추가
        if(buffer.size() < N){
            buffer.push(packet);
        }else{
            // 버려짐
        }
    }

    if(buffer.empty()){
        cout << "empty\n";
    }else{
        while(!buffer.empty()){
            cout << buffer.front() << " ";
            buffer.pop();
        }  
        cout << "\n";
    }
}
