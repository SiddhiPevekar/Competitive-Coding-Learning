def Selection_sort(array):
    #we need to keep track of current one in unsorted sublist
    currentIdx = 0
    while currentIdx <= len(array)-1:
        #-1 as iterator started from 0 --> currentIdx = 0
        smallestIdx = currentIdx
        for i in range(currentIdx+1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        #now once we have smallest we can swap the numbers
        swap(currentIdx, smallestIdx, array)
        currentIdx+=1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [8,5,2,9,5,6,3]
print(Selection_sort(array))