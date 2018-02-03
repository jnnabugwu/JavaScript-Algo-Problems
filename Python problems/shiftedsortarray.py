
# find target number in a array of sorted numbers but it is rotated at a pivot point.
def shiftsortarray(array,target):#O(log(N)) + O(N)
    pivot = findpivot(array)
    found_it = (binarysearch(array,0,pivot,target))
    if found_it >= 0:
        return found_it
    else:
        found_it = binarysearch(array,pivot+1,len(array),target)
        return found_it
def binarysearch(array,left,right,target): #O(Log(N))
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid-1
        else: 
            left = mid + 1
    return -1  
def findpivot(array):#0(N)
    for i in range(1,len(array)):
        if array[i-1] > array[i]:
            return i-1
# print(shiftsortarray([12,16,17,1,4,8,9,11],0))
# print(shiftsortarray([12,16,17,1,4,8,9,11],1))
#Merge two lists O(N+M) ;N = the number of elements in first array, M = number of elements in second array
def merge2lists(array,array2):
    array3 = []

    while 0 <len(array) or 0 < len(array2):
        # try to use poping
        if len(array) == 0:
            array3.append(array2.pop(0))   
        elif len(array2) == 0:
            array3.append(array2.pop(0))
        elif array[0] < array2[0]: #if the the element in the first array is less
            array3.append(array.pop(0))
        elif array[0] > array2[0]:
            array3.append(array2.pop(0))
        elif array[0] == array2[0]:
            array3.append(array.pop(0))
            array3.append(array2.pop(0))
    return array3        
print(merge2lists([1,3,5,6],[2,4,8,9,10]))



