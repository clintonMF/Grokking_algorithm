# thought process for creating the sorting algorithm
# create a function to find the position of the smallest number
# the array.



def findSmallest(arr):
    """
    this function returns the index of the smallest function
    in the array.
    """
    position = 0
    # the variable position is used to set the initial index of the 
    # smallest number to 0. it will be compared to other numbers of
    # array and changed appropriately.
    for i in range(1,len(arr)):
        # we loop through the entire array from index 1 to the len(arr).
        # we start from index 1 because we to index of 0.
        if arr[i] < arr[position]:
            position = i
    return position
        


def selectSort(arr):
    """ 
    this function is used to arrange the elements of an array in
    ascending order.
    """
    sorted_list = []
    # the sorted_list variable would help house the element as they get sorted.
    while len(arr) > 0:
        smallestNum = findSmallest(arr)
        position = arr.pop(smallestNum)
        sorted_list.append(position)
    return sorted_list

g = selectSort([1,7,1,2,5,3,6,8,9])

print(g)
        