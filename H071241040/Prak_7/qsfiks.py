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

array = [1, 8, 20, 7, 9, 11, 13, 1, 3, 2, 1, 4, 3, 2, 5]
sorted_array = quick_sort(array)
print("Array yang diurutkan:", sorted_array)


