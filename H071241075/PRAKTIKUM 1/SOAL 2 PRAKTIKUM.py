
karakter = input("Masukkan karakter: ")
kalimat = input("Masukkan kalimat: ")

pesan_dict = {
    0: f"{karakter} tidak ditemukan dalam {kalimat}",
    1: f"{karakter} merupakan bagian dari {kalimat}"
}

count = kalimat.count(karakter)

print(pesan_dict[int(count > 0)])