#Bubble sort algorithm

from typing import Counter


def BubbleSort(array):
    isSorted = False
    Counter=0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - Counter):
            #len-1 bcz we don't to go again and again till end as it will be already sorted
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted= False
        Counter+=1
            #it does't affect time complexity but is for better practice
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [8,5,2,9,5,6,3]
print(BubbleSort(array))