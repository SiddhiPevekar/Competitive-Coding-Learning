def merge_sort(array):
    if len(array)==1:
        return array 
    middleIdx = len(array)//2
#// -->to roundoff
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArrays(merge_sort(leftHalf), merge_sort(rightHalf))

def mergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf)+len(rightHalf))
    k=i=j=0
    while i< len(leftHalf) and j< len(rightHalf):
        if leftHalf[i]<=rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i+=1
        else:
            sortedArray[k] = rightHalf[j]
            j+=1
        k+=1
    while i<len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i+=1
        k+=1
    while j<len(leftHalf):
        sortedArray[k] = rightHalf[j]
        j+=1
        k+=1
    return sortedArray


array = [8,5,2,9,10,5,6,3]
print(merge_sort(array))