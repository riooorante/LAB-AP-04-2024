karakter = input("Masukkan karakter yang ingin dicari: ")
kalimat = input("Masukkan kalimat: ")

pesan = "merupakan bagian dari" * (karakter in kalimat) + "tidak ditemukan dalam" * (karakter not in kalimat)

print(f'{karakter} {pesan} "{kalimat}"')