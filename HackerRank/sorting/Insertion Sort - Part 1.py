def insertionSort1(arr):
    n = 0
    indx = 0
    while n < len(arr):
        if n != 0 and arr[n] < arr[n-1] and arr[n] > arr[n-1]:
            indx = n
            break
        elif n != len(arr) and arr[n] > arr[n+1] and arr[n] > arr[n-1]:
            indx = n + 1
            break
        else:
            n += 1
    print(indx, arr[indx])

lista = [1,2,8,3,4,5,6,7,9]
insertionSort1(lista)
