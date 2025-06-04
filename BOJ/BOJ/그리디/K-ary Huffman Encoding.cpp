#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

// 최대 문자의 종류 10000
int T;
int N,K;


struct Node{
    
    vector<Node*> children;
    int data = -1;
    int cnt = 0;
};

struct cmp {
    bool operator()(const Node* _Left, const Node* _Right) const{
        return _Left->cnt > _Right->cnt;
    };
};


int solve();
int recursive(Node* cur, int depth);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;
    for(int i = 0; i < T; i++){
        cout << solve() << "\n";
    }
}



Node leafs[100'001];
Node* root;

int solve(){
    priority_queue<Node*,vector<Node*>, cmp> pq;
    cin >> N >> K;
    for(int i = 0; i < N; i++)
    {
        leafs[i].data = i;
        cin >> leafs[i].cnt;
        pq.push(&leafs[i]);
    }
    while((pq.size()) % (K-1)){
        Node* dummy = new Node;
        dummy->data = -10;
        pq.push(dummy);
    } 

    while(pq.size()>= 2){
        Node* parent = new Node;
        while(!pq.empty() && parent->children.size() < K){
            Node* child = pq.top(); pq.pop();

            parent->children.push_back(child);
            parent->cnt += child->cnt;
        }
        pq.push(parent);
    }
    root = pq.top();
    pq.pop();

    int ans = recursive(root, 0);
    return ans;
}

int recursive(Node* cur, int depth){
    if(cur->children.size() == 0){
        cout << cur->cnt << " " << depth << "\n";
        return cur->cnt * depth;
    }
    int ans = 0;
    for(int i = 0; i < cur->children.size(); i++){
        ans += recursive(cur->children[i], depth + 1);
    }
    return ans;
}