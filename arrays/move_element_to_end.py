#O(n) time| O(1) Space
def move_Element_to_end(array, toMove):
    i=0
    j = len(array)-1
    while i<j:
        while array[j]== toMove:
            j-=1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i+=1
    return array

array=[2,4,3,8,2,2,2,3,2]
toMove=2
print(move_Element_to_end(array, toMove))