array = [1,2,5,7,8,78,100]
key = 7

low = 0
up = len(array) - 1

while low <= up:
    med = (low + up) // 2
    if array[med] == key:
        print(f"Angka yang dicari berada di posisi ke-{med}")
        break
    else:
        if array[med] < key:
            low = med + 1
        else:
            up = med - 1