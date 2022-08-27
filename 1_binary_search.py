def binary_search(list, item):
    """An iterative function that implements binary search"""
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2 
# double slash is used as opposed to single slash
# because in python a single slash is a classic division while 
# double slash is floor division (it rounds down to the nearest whole number).

        guess = list[mid]
        # check if the number = middle term
        if guess == item:
            return mid
        # check if the number is greater than the 
        # middle term
        if guess > item:
            high = mid - 1
        # if the number is less than the middle term
        else:
            low = mid + 1
    return None


# the function above is an iterative function and the preferred way of
# implementing binary search. there is also a recursive way to use binary_search 



def binary(lst,lw,hi,n):
    """
    A recursive function that implements binary search
    """
    # Check base case
    if hi >= lw:
        mid = (hi + lw)//2
        guess = lst[mid]
        
        # If element is present at the middle itself
        if guess == n:
            return mid
        # If element is smaller than mid, then it
        # can only be present in left sub array
        elif guess < n:
            return binary(lst,mid + 1,hi,n)
        # Else the element can only be present
        # in right sub array
        else:
            return binary(lst,lw,mid - 1,n)
    # Element is not present in the array
    else:
        return None 
    
my_list = [1,2,3, 5, 7, 9]

# answer = binary(my_list,0, len(my_list),2)
answer = binary_search(my_list,2)

print(answer) 