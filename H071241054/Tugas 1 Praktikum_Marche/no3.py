#Input jumlah detik
detik = int(input("Masukkan jumlah detik: "))

#Menghitung konversi
jam = int(detik//3600)                # 1 jam = 3600 detik
menit = int(detik % 3600)//60        # Sisa detik setelah diambil 1 jam dibagi 60 untuk menit
detik = int(detik % 60)              # Sisa detik setelah diambil jam dan menit

#Output
print(f"{jam}:{menit}:{detik}")