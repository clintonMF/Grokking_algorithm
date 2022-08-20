# this file would be divided into 2 section 


# --------------------------------------------------#
# 1. Divide and conquer algorithms.
#  divide and conquer is a technique for solving problems in computer 
# science that involves breaking a problem into smaller instances. 
# it sounds similar to recursive functions thats because recursive functions 
# are employed in solving divide and conquer problems.
# Divide and conquer was employed in creating the recursive function for binary
# search in chapter 1. 
# Divide and conquer gives you a new way of thinking about problems.
# below there are examples 
# -------------------------------------------------#

# the example below uses divide and conquer to get the sum of elements
# in a list.
# Exercise 4.2

def sumList(arr):
    length = len(arr)
    if  length == 1:
        return arr[0]
    else:
        return arr[0] + sumList(arr[1:])
    
    
arr = [1,2,3,4,5,6]
s = sumList(arr)
print(s)


# NOTE
# the function above can be easily written with a loop i.e iteration
# Exercise 4.1
def sumList_iter(arr):
    sum = 0 
    for i in arr:
        sum += i 
    return sum 

# the function below finds the maximum number in a list
# exercise 4.3

def max_num(arr):
    max_ind = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_ind]:
            max_ind = i
    return arr[max_ind]

print(max_num(arr))
# this is the recursive version
def max_rec(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    
    sub_max = max_rec(arr[1:])
    
    return arr[0] if arr[0] > sub_max else sub_max

print(max_rec(arr))


# #################################################################
# quicksort is a sorting algorithm one of the most used sorting algorithm
# on average it is faster than select sort algorithm but they have the same 
# worst case scenario of 0(n square). quicksort makes use of divide and conquer 
# technique and makes use of inductive proof which consists of base case and 
# inductive case.
# In quicksort algorithm we make use of a pivot this pivot is used to partition the
# list (ie divide it into 2 different parts). usually of numbers greater than the
# pivot and numbers less than the pivot.
# The speed of the quick sort algorithm depends on the pivot chosen. If the pivot
# chosen is closed to the median of the list this is the best case scenario. if the 
# pivot chosen is the highest or lowest number in the list this is the worse case 
# scenario. the big 0 of the best and worst case scenario are 0(nlogn) and 0(n square)
# respectively.
# A quick sort algorithm is shown below.
# #################################################################

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        
        return quickSort(less) + [pivot] + quickSort(greater)
    
l = [1,3,45,6,5,6]
f= quickSort(l)

print(f)