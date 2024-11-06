
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]  
    middle = [x for x in array if x == pivot]  
    right = [x for x in array if x > pivot]  
    return quick_sort(left) + middle + quick_sort(right)
array = [33, 10, 68, 19, 5, 14, 42]
hasil = quick_sort(array)
print("Array yang diurutkan:", hasil)
