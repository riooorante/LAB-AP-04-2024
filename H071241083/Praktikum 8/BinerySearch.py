def binary_search(arr, cari_nilai):
    
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        nilai_mid = arr[mid]
        
        if nilai_mid == cari_nilai:
            return mid
        elif nilai_mid < cari_nilai:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
    
arr = [1,2,2,4,6,7,8,9]
cari_nilai = 4
hasil = binary_search(arr, cari_nilai)

if hasil != -1:
    print(f"Elemen {cari_nilai} ditemukan di indeks {hasil}.")
else:
    print(f"Elemen {cari_nilai} tidak ditemukan.")