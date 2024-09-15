karakter = input("Masukkan karakter yang ingin dicari: ")
kalimat = input("Masukkan kalimat: ")

print((f"{karakter} merupakan bagian dari {kalimat}", 
       f"{karakter} tidak ditemukan dalam {kalimat}")[karakter not in kalimat])