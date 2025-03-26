#include <iostream>
// #include <bitset>

using namespace std;

int N,M;
int labels[101];
int predict[16][101];

int get_sum(int arr[],int N){
    int res = 0;
    for (size_t i = 0; i < N; i++)
    {
        res += arr[i];
    }
    return res;
}

bool is_ok(int maximum, int flags){
    int cnt[101] = {0,};
    int choosed_model_amount = 0;
    // cout << bitset<4>(flags) << endl;
    for (int model = 0; model < N; model++)
    {
        if(flags & (1 << model)){
            choosed_model_amount++;
            for (int j = 0; j < M; j++)
            {
                cnt[j] += predict[model][j];
            }
        }
    }
    if(choosed_model_amount % 2 == 0){
        return false;
    }
    int ok_cnt = 0;
    for (int j = 0; j < M; j++)
    {
        // cout << cnt[model] << endl;
        if(cnt[j] > choosed_model_amount/2){
            ok_cnt++;
        }
    }
    // cout << "ok :" << ok_cnt << endl;
    if(ok_cnt > maximum)
        return true;
    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        cin >> labels[i];
    }
    int maximum = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> predict[i][j];
            predict[i][j] =  (int)(predict[i][j] == labels[j]);
            // cout << i << " " << j << " : " << predict[i][j] << endl;
        }
        maximum = max(maximum, get_sum(predict[i], M));
    }
    // cout << "Max : " << maximum << endl;
    for (int i = 0; i < (1 << N); i++)
    {
        if(is_ok(maximum, i)){
            cout << 1 << endl;
            return 0;
        }
    }
    
    cout << 0 << endl;

    return 0;
}