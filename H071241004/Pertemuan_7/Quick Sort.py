def quick_sort(angka):
    if len(angka) <= 1:
        return angka
    else:
        pivot = angka[len(angka) // 2]
        kiri = [x for x in angka if x < pivot]
        tengah = [x for x in angka if x == pivot]
        kanan = [x for x in angka if x > pivot]
        return quick_sort(kiri) + tengah + quick_sort(kanan)

angka = [9, 8, 7, 6.20, 5.30,9, 10, 78.9]
print(quick_sort(angka))
