def binary(arr, target):
    low, high = 0 , len(arr)-1
    while low<=high:
        mid = (low + high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high = mid - 1
        elif arr[mid]<target:
            low = mid + 1
    return -1

arr = [5,3,2,3,1,2,3,5,7,7,0,9,8,7,6,5]
target = 0

hasil = binary(arr, target)
if hasil != -1:
    print(hasil)

else:
    print("tidak ada")