harga_hari_ini = 105.0
harga_kemarin = float(input("Masukkan harga saham kemarin: "))

# Menghitung persentase perubahan
perubahan_persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

# Menentukan indeks rekomendasi berdasarkan persentase perubahan
index = (perubahan_persen > 5) * 0 + (-3 <= perubahan_persen <= 5) * 1 + (perubahan_persen < -3) * 2

rekomendasi_123 = ("Beli", "Tahan", "Jual")

# Mengambil rekomendasi berdasarkan indeks
rekomendasi = rekomendasi_123[index]

# Menampilkan perubahan persentase harga dan rekomendasi
print(f"Perubahan persentase harga: {perubahan_persen:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi}")