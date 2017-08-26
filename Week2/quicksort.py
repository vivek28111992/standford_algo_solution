def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        #print(myList[pivot])
        # sort both halves
        quicksort(myList, start, pivot-1)
        #print(myList)
        quicksort(myList, pivot+1, end)
        #print(myList)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    #print('pivot ', pivot)
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while right >= left and myList[right] >= pivot:
            right = right - 1
        if right < left:
            done = True
        else:
            #swap places
            temp = myList[left]
            myList[left] = myList[right]
            myList[right] = temp
            #print(myList)

    # swap start with myList[right]
    temp = myList[start]
    myList[start] = myList[right]
    myList[right] = temp
    #print(myList)
    return right


array = [line.rstrip('\n') for line in open('../QuickSort.txt')]
array = list(map(int, array))
print(quicksort(array, 0, len(array) - 1))
