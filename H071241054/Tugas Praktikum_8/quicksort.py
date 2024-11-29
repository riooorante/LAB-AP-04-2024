def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array)//2]
        kiri = [x for x in array if x < pivot]
        tengah = [x for x in array if x == pivot]
        kanan = [x for x in array if x > pivot]

        return quick_sort(kiri) + tengah + quick_sort(kanan)

array = [3, 1, 5, 2, 13, 9, 11]
print(quick_sort(array))