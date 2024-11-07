def binary_search(arr, target):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1

data = [2,3,6,7,9,11,14,17]
target = 9
hasil = binary_search(data,target)
if hasil != -1:
    print(f"elemen ditemukan pada {hasil}")
else:
    print("elemen tidak ditemukan")