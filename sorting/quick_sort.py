def quick_sort(array):
    quick_sort_helper(array, 0, len(array)-1)
    return array
def quick_sort_helper(array, startIdx, endIdx):
    if startIdx > endIdx:
        return
    pivot = startIdx
    leftIdx = startIdx+1
    rightIdx = endIdx
    while rightIdx>= leftIdx:
        if array[leftIdx]>array[pivot] and array[rightIdx]<array[pivot]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx]<= array[pivot]:
            leftIdx+=1
        if array[rightIdx] >= array[pivot]:
            rightIdx-=1
    swap(pivot, rightIdx, array)
    leftSubarrayIsSmaller = rightIdx -1-startIdx < endIdx-(rightIdx+1)
    if leftSubarrayIsSmaller:
        quick_sort_helper(array, startIdx, rightIdx-1)
        quick_sort_helper(array, rightIdx+1, endIdx)
    else:
        quick_sort_helper(array, rightIdx+1, endIdx)
        quick_sort_helper(array, startIdx, rightIdx-1)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [8,5,2,9,5,6,3]
print(quick_sort(array))