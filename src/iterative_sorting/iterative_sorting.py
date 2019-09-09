# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        sorted_index = i
        smallest_index = i
        for j in range(sorted_index+1, len(arr)):
            current_index = j
            if arr[smallest_index] > arr[current_index]: 
                arr[smallest_index], arr[current_index] = arr[current_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        sorted_round=False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted_round = True
        if not sorted_round:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr