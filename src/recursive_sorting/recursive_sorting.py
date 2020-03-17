# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    a, b, m = 0, 0, 0

    while m < elements:
        if a >= len(arrA) or b >= len(arrB):
            break
        elif arrA[a] < arrB[b]:
            merged_arr[m] = arrA[a]
            a += 1
        elif arrB[b] < arrA[a]:
            merged_arr[m] = arrB[b]
            b += 1
        m += 1

    while a < len(arrA):
        merged_arr[m] = arrA[a]
        m += 1
        a += 1

    while b < len(arrB):
        merged_arr[m] = arrB[b]
        m += 1
        b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        arr1 = merge_sort(arr[:mid])
        arr2 = merge_sort(arr[mid:])
        return merge(arr1, arr2)

    return arr


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
