import heapq

arr = []
for i in range(10,1,-1):
    for j in range(10,1,-1):
        arr.append([i,j])

heapq.heapify(arr)
print(arr)