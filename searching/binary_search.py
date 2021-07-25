def binary_search(array, search):
    # leftIdx = 0
    # rightIdx = len(array)-1
    return searchHelpler(array, search, 0, len(array)-1)

def searchHelpler(array, search, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return -1
    #if leftIdx > rightIdx:
    #   return -1 instead of this we can use while leftIdx<rightIdx and atlast return -1
    middleIdx = (leftIdx+rightIdx)//2
    potentialMatch = array[middleIdx]
    if search == potentialMatch:
        return middleIdx
    elif search<potentialMatch:
        return searchHelpler(array, search, leftIdx, middleIdx-1)
    else:
        return searchHelpler(array, search, middleIdx+1, rightIdx)

array = [7,11,44,54,78,89,95,97,100]
search=100
print(binary_search(array,search))