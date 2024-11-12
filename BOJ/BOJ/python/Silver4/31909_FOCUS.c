#include <stdio.h>


int arr[];
int N,K,cmd;

void main(){
    int a,b;
    scanf("%d", &N);
    for (size_t i = 0; i <= 7; i++)
    {
        arr[i] = i;
    }
    for (size_t i = 0; i < N; i++)
    {
        scanf("%d",&cmd);
        if(!decode(cmd,&a,&b))
            continue;
        swap(arr[a],arr[b]);
    }

    scanf("%d",&K);
    
}

void swap(int* a,int* b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int decode(int raw, int* a, int* b){
    size_t i;
    for (i = 7; i >= 0; i--)
    {
        if(raw >= (1 << i)){
            raw -= (1 << i);
            *a = i;
            break;
        }
    }
    for (; i >= 0; i--)
    {
        if(raw >= (1 << i)){
            raw -= (1 << i);
            *b = i;
            break;
        }
    }
    if(raw) return 0;
}