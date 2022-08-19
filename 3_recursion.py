# recursion is a programming technique which solves a problem by 
# solving smaller instances of the same problem.
# a recursive function is usually one that calls itself.
# we try to decrease the input size with each call.
# recursive function usually consist of 2 parts
# 1. the base case 
# 2. the recursive case
# examples are below.

# A recursive function for factorial.
def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

# a recursive function for binary_search.
def binary_search(arr,low,high,item):
    mid = (low + high)//2
    guess = arr[mid]
    if guess == item:
        return mid
    elif guess > item:
        return binary_search(arr,low,mid -1, item)
    elif guess < item:
        return binary_search(arr,mid + 1, high,item)
    else:
        return None
    
arr = [1,2,3,4,5]

p = binary_search(arr,0,len(arr),2)

print(p)

# a recursive function to count the number of items in an array
def arrayItemCount(arr):
    if len(arr) < 1:
        return 0
    else:
        return 1 + arrayItemCount(arr[1:])
    
arr = [1,2,3,4,5,6]

print(arrayItemCount(arr))
