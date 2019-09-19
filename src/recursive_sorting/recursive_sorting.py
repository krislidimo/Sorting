# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    hasArrA = len(arrA) >= 1
    hasArrB = len(arrB) >= 1
    # TO-DO

    while hasArrA and hasArrB:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
        hasArrA = len(arrA) >= 1
        hasArrB = len(arrB) >= 1

    # If one is empty but the other still has numbers
    while hasArrA or hasArrB:
        if hasArrA:
            merged_arr.append(arrA.pop(0))
        elif hasArrB:
            merged_arr.append(arrB.pop(0))
        hasArrA = len(arrA) >= 1
        hasArrB = len(arrB) >= 1

    return merged_arr

# print(merge([1,3],[2,4,5, 9, 10]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    mid = int(len(arr)/2)
    arrA = arr[:mid] # [1,2,3] 
    arrB = arr[mid:] # [4,5,6]

    if len(arrA) > 1:
        arrA = merge_sort(arrA) 
    if len(arrB) > 1:
        arrB = merge_sort(arrB)

    arr = merge(arrA, arrB)

    return arr

print(merge_sort([2,7,5,9,1,4,3]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
