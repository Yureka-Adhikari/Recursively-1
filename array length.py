def array_length(arr):
    if not arr:
        return 0
    return 1 + array_length(arr[1:])

arr = [8,4,5,6,7,3,2,1]
print(f"Length of the array is = {array_length(arr)}")