def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = []
    middle = []
    right = []
    for x in array:
        if x < pivot:
            left.append(x)     
        elif x == pivot:
            middle.append(x) 
        else:
            right.append(x)
    return quick_sort(left) + middle + quick_sort(right)

array = [1, 8, 20, 7, 9, 11, 13,1,3,2,1,4,3,2,5]
sorted_array = quick_sort(array)
def binary_search(list, target):
    sisi_kiri = 0
    sisi_kanan = len(list) - 1 
    while sisi_kiri <= sisi_kanan:
        mid = (sisi_kiri + sisi_kanan) // 2  
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            sisi_kiri = mid + 1 
        elif list[mid]> target:
            sisi_kanan = mid - 1  
    return -5
print(f"Array Terurut- {sorted_array}")
list = sorted_array
target = 11
result = binary_search(list, target)
if result != -5:
    print(f"Target found at index {result}")
else:
    print("Target not found in the list")
