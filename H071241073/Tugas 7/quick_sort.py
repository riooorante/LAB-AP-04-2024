def quick_sort(data):
    panjang = len(data)

    if panjang < 1:
        return data
    else:
        pivot = data.pop()

    kurang_dari = []
    lebih_dari = []

    for i in data :
        if i > pivot:
            lebih_dari.append(i)
        else :
            kurang_dari.append(i)
    return quick_sort(kurang_dari) + [pivot] + quick_sort(lebih_dari)

print(quick_sort([7,10,2,4,5,8,4,89,3,9]))
             