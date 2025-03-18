#include "bogoSort.h"
#include <vector>
#include <algorithm>
#include <iostream>

bool is_ok(int N, std::vector<int> &b);

void sort_array(int N){
    std::vector<int> arr = copy_array();
    // std::vector<int> ans = copy_array();
    // std::sort(ans.begin(),ans.end());
    int start;
    start = 0;
    while(!is_ok(N,arr)){
        std::cout << start << std::endl;
        int target = start;
        while(arr[start] != target){
            // std::cout << start << " " << end << std::endl;
            int end = start;
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
    for (size_t i = 0; i < N; i++)
    {
        if(a[i] != i)
            return false;
    }
    return true;
}