#include <iostream>
#include <cmath>

using namespace std;

int K;
int factors[11];
int a,b,N;
double target;
double delta_x;

double integral(int x){
    // 적분상수 제외
    double res = 0;
    for(int i = K, pw = 1;i >= 0; i--, pw++){
        double tmp = factors[i] / (double) pw;
        // cout << pw << ": "<< x << "  "<<factors[i] << " "<< tmp << endl;
        res += tmp * pow(x,pw);
    }
    return res;
}

double calc(double x){
    double res = 0;
    // cout << "calc : " << (x) << endl;
    for(int i = K, pw = 0; i >= 0; i--, pw++){
        res += factors[i] * pow(x,pw);
    }
    return res;
}

double almost(double e){
    double total = 0;
    for(int i = 0; i <= N - 1; i ++){
        // cout << a + i * delta_x + e << endl;
        total += calc(a + i * delta_x + e) * delta_x;
    }
    return total;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    cin >> K;
    for(int i = 0; i <= K; i ++){
        cin >> factors[i];
    }
    cin >> a >> b >> N;
    delta_x = (b-a) / (double)N;

    
    target = integral(b) - integral(a);

    double current,mid;
    int x;
    double low = 0, high = delta_x;
    while(low < high){
         mid = low +(high - low) / 2;
        // cin >> x;
        // cout << "l " << low << " h " << high << endl;
        current = almost(mid);
        double distance = (target - current);
        // cout << distance << endl;
        if(fabs(distance) <= 0.0001){
            break;
        }
        else if(distance > 0){
            low = mid;
        }else{
            high = mid;
        }
    }
    cout << mid << endl;
    return 0;
}