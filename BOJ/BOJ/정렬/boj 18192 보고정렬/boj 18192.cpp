#include "bogoSort.h"
#include <vector>
bool is_ok(int N, std::vector<int> &b);

void sort_array(int N){
    std::vector<int> arr = copy_array();
    int start;
    start = 0;
    while(!is_ok(N,arr)){
        // std::cout << start << std::endl;
        int target = start;
        while(arr[start] != target){
            int end = start + 1;
            for(; end < N; end++){
                if(arr[end] == target)
                    break;
            } 
            shuffle_array(start,end);
            arr = copy_array();
        }
        // 끌어내리기 성공
        // 다음놈 끌어내리러 가자
        start++;
    }

    return;
}

bool is_ok(int N, std::vector<int> &a){
    for (int i = 0; i < N; i++)
    {
        if(a[i] != i)
            return false;
    }
    return true;
}