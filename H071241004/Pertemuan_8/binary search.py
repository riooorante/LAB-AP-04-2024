def binarysearch(data, target):
    kiri = 0
    kanan = len(data) - 1

    while kiri <=  kanan:
        tengah = (kiri +  kanan) // 2

        if data[tengah] == target:
            return tengah
        
        if data[tengah] < target:
            kiri = tengah+ 1
        else:
            kanan = tengah - 1

    return -1

data = [1,3,5,7,9,11,13,15,17,19]
target = 11

print(binarysearch(data, target))