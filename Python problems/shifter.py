from collections import deque
def shifter(a,n,k):
    tem = deque()
    for i in range(0,k):
        tem.appendleft(a[i])
    for i in range(k,len(a)):
        a[i-k] = a[i]
    for i in range(len(a)-k,len(a)):
        a[i] = tem.popleft()
    # i = k-1    
    # while len(tem)!=0:
    #     a[i] = tem.popleft()
    #     i += 1
    return a
print(shifter([1,2,3,4,5],5,4))
print(shifter([1,2,3,4,5,6,7,8],8,4))  

