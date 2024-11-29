def binary_search(data, cari):
    indeks = 0
    indeks_akhir = len(data) - 1

    while indeks <= indeks_akhir:
        titik_tengah = indeks + indeks_akhir  // 2
        nilai_titiktengah = data[titik_tengah]  
        if nilai_titiktengah == cari:
            return titik_tengah
        elif cari < nilai_titiktengah:
            indeks_akhir = titik_tengah - 1
        else:
            indeks = titik_tengah + 1

    return None

data_a = [0,1,2,3,8,9]
cari_a = int(input("Masukkan yang ingin dicari: "))
print(binary_search(data_a, cari_a))