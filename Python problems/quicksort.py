def partition(array,left,right):
    
        pivot = array[left]
        leftmarker = pivot + 1
        rightmarker = right
        while True:
            while array[leftmarker] < pivot and array[rightmarker] > array[leftmarker]:
                leftmarker += 1
            while array[rightmarker] > pivot and array[rightmarker] > array[leftmarker]:    
                rightmarker -= 1
            while rightmarker > leftmarker:
                break    
            if array[leftmarker] > array[rightmarker]:
                temp = array[rightmarker]
                array[rightmarker] = array[leftmarker]
                array[leftmarker] = temp
                leftmarker +=1
                rightmarker -=1
        temp = pivot
        array[left] = pivot
        array[rightmarker] = temp
        return rightmarker
def quicksorthelper(array,left,right):
    if left < right:
        index = partition(array,left,right)
        quicksorthelper(array,left,index)
        quicksorthelper(array,index+1,right)

def quicksort(array):
    quicksorthelper(array,0,len(array)-1)
    return array
    

    
    
print(quicksort([2,4,3,0,13,7,27,18]))                    
