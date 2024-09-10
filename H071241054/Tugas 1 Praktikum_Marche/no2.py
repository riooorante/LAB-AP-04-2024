#input
karakter = str(input("Masukkan karakter: "))
kalimat = str(input("Masukkan kalimat: "))

#Menggunakan operator "in" untuk memeriksa keberadaan karakter
pesan = ["tidak ditemukan dalam", "merupakan bagian dari"][karakter in kalimat]

#Menampilkan pesan
print(f"'{karakter}'{pesan}'{kalimat}'")