#include <iostream>


using namespace std;

int N;

int A[10'001];
int B[10'001];

bool ans = false;
int cnt = 0;
void check(){
    if(cnt == N){
        ans = true;
    }
}

void SWAP(int a, int b){
    int temp = A[a];
    cnt -= (A[a] == B[a]) + (A[b] == B[b]);
    A[a] = A[b];
    A[b] = temp;
    cnt += (A[a] == B[a]) + (A[b] == B[b]);
    check();
    
}

// void printA(){
//     for(int i = 0; i < N; i++){
//         cout << A[i] << " ";
//     }
//     cout << "\n";
// }


int partition(int left, int right){
    int pivot = A[right];
    int i = left - 1;
    for(int j = left; j < right; j++){
        if(A[j] <= pivot){
            i++;
            SWAP(i, j);
            // printA();
            // cout << cnt << "\n";
        }
    }
    SWAP(i + 1, right);
    return i + 1;
}

void quickSort(int left, int right){
    if(right <= left || ans)
        return;
    int p = partition(left, right);
    quickSort(left, p - 1);
    quickSort(p + 1, right);
}



int main(){
    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    for(int i = 0; i < N; i++){
        cin >> B[i];
        if(A[i] == B[i]){
            cnt++;
        }
    }
    check();

    if(ans){
        cout << 1 << "\n";
        return 0;
    }
    quickSort(0, N - 1);
    if(ans){
        cout << 1 << "\n";
    }else{
        cout << 0 << "\n";
    }
    return 0;
}

