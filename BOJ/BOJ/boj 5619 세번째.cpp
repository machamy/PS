#include <iostream>
#include <algorithm>
#include <vector>
#include <string>


using namespace std;

int N;
int counts[10001];

/*
3, 11 
-> 113

2 4 5 11

24
25
26 <<


1. 길이순으로 정렬
2. 길이가 같다면 맨앞을 기준으로 정렬
--> 그냥 정렬이랑 똑같네
앞에서 3개 뽑고
모두 같은 자리수면 걍 뒤에 두개로 한거
다른 자리수면 다 만들고 정렬하기
*/
int main(){
    cin >> N;
    for(int i = 0; i< N; i++){
        int n;
        cin >> n;
        counts[n]++;
    }
    vector<int> candidates;
    for(int i = 1; i <= 10000; i++){
        while(counts[i] && candidates.size() < 4){
            candidates.push_back(i);
            counts[i]--;
        }
        if(candidates.size() >= 4){
            break;
        }
    }

    vector<int> nums;
    // 3개의 숫자들로 만들 수 있는 모든 조합을 구한다.
    // 문자열 변경 -> 합치기 -> 정렬
    string a = to_string(candidates[0]);
    string b = to_string(candidates[1]);
    string c = to_string(candidates[2]);

    nums.push_back(stoi(a + b));
    nums.push_back(stoi(a + c));
    
    nums.push_back(stoi(b + a));
    nums.push_back(stoi(b + c));
    nums.push_back(stoi(c + a));
    nums.push_back(stoi(c + b));

    if(candidates.size() == 4){
        string d = to_string(candidates[3]);
        nums.push_back(stoi(a + d));
        nums.push_back(stoi(b + d));
        nums.push_back(stoi(c + d));
        nums.push_back(stoi(d + a));
        nums.push_back(stoi(d + b));
        nums.push_back(stoi(d + c));

    }
    // 정렬
    sort(nums.begin(), nums.end());

    cout << nums[2] << endl; // 3번째로 큰 수 출력


    return 0;
}