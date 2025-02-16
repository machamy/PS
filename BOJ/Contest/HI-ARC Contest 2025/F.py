import heapq

N = int(input())
A = list(map(int,input().split()))
if N == 2:
    exit()
class LinkedList:
    def __init__(self,array):
        self.head = Node()
        prev = self.head
        for idx,e in enumerate(array):
            n = Node(idx + 1,e)
            prev.next = n
            n.prev = prev
            prev = n
    def pop(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        for l in node.e:
            l[3] = True
        # for l in node.prev.e:
        #     l[3] = True
        # for l in node.next.e:
        #     l[3] = True
class Node:
    def __init__(self,idx = -1, v = None):
        self.prev = None
        self.next = None
        self.idx = idx
        self.value = v
        self.e = []
# (delta,a,b,c) 를 저장함
# b 추방시, delta z a c와 delta a c d 를 추가함
# 정렬을 위해서 delta, b, a, c 로 저장
L = LinkedList(A)
hq = [None for _ in range(N-2)]
n = L.head.next.next
idx = 0
while n.next != None:
    a,b,c = n.prev.value,n.value,n.next.value
    d = abs(c - a)
    hq[idx] = [d,b,n,False,n.prev.idx,n.next.idx]
    # n.prev.e.append(hq[idx])
    n.e.append(hq[idx])
    # n.next.e.append(hq[idx])
    idx += 1
    n = n.next
# print(hq)
heapq.heapify(hq)
out = [False for _ in range(100_001)]
while hq:
    # print("----")
    # print(hq)
    delta,b,b_node, flag,a_idx,c_idx = heapq.heappop(hq)
    if flag or out[a_idx] or out[c_idx]:
        continue
    # print(b_node)
    print(b_node.idx,delta)
    out[b_node.idx] = True
    L.pop(b_node)
    a = b_node.prev
    c = b_node.next
    z = b_node.prev.prev
    d = b_node.next.next
    if z != None and z.value != None:
         # z a c
         heapq.heappush(hq,[abs(c.value-z.value),a.value,a,False,z.idx,c.idx])
    if d != None:
         # a c d
        #  print("sss ",a.value,d.value)
         heapq.heappush(hq, [abs(a.value-d.value),c.value,c,False,a.idx,d.idx])
        #  print([abs(a-d.value),c,b_node.next])
