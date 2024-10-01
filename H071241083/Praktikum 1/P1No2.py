#Memeriksa karakter
karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan kalimat: ")

hasil = f'{karakter} merupakan bagian dari "{kalimat}"' * (karakter in kalimat) or f'{karakter} tidak ditemukan dalam "{kalimat}"'

print(hasil)