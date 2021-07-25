def three_largest_numbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftUpdate(threeLargest, num, 0)

def shiftUpdate(array, num, Idx):
    for i in range(Idx+1):
        if i ==Idx:
            array[i] = num
        else:array[i] = array[i+1]


array=[189,54,-181,74,14,-45,541,144]
print(three_largest_numbers(array))