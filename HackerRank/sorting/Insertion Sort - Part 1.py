def insertionSort1(arr):
    arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    n = len(arr)
    num = arr[n - 1]
    for j in range(len(arr)-2, -1, -1):
        if arr[j] < num:
            arr[j+ 1] = num
            break
        arr[j+1] = arr[j]
    if arr[0] > num:
        arr[0] = num
    print(arr)
       