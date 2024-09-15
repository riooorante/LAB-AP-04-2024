#Input harga saham kemarin
saham_kemarin = float(input("Masukkan harga saham kemarin: "))

saham_hari_ini = 105.0
rekomendasi = ["Beli", "Tahan", "Jual"]

#Menghitung perubahan persentase harga saham
perubahan_persentase = ((saham_hari_ini - saham_kemarin)/saham_kemarin)*100
hasil = rekomendasi[(perubahan_persentase > -3)+(perubahan_persentase > 5)]

#Menampilkan hasil
print(f"Rekomendasi persentase harga saham:{perubahan_persentase:.2f}%")
print(f"Rekomendasi investasi: {hasil}")