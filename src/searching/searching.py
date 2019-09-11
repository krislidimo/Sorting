# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  while True:
    if len(arr) == 0:
      break # array empty

    low = 0
    high = len(arr)-1
    mid = int((high - low)/2)
    
    if arr[mid] == target:
      return mid # found target
    elif arr[mid] > target:
      arr = arr[low:mid+1]
    else:
      arr = arr[mid:high+1]

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  mid = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty

  if arr[mid] == target:
    return mid # target found
  elif arr[mid] > target:
    return binary_search_recursive(arr[0:mid+1], target, low, mid)
  else:
    return binary_search_recursive(arr[mid:len(arr)+1], target, mid, high)
