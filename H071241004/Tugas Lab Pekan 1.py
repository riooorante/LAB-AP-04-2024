#Rekomendasi Saham
harga_hari_ini = 105.0
harga_kemarin = float(input('Masukkan harga saham kemarin : '))
rumus = (harga_hari_ini - harga_kemarin) / harga_kemarin * 100
d = 'Beli' * (rumus > 5) + 'Tahan' * (5 >= rumus >= -3) + 'Jual' * (rumus < -3)
print(f'Perubahan persentase harga saham : {rumus :.2f}%')
print(f'Rekomendasi investasi : {d}')

#Memeriksa karakter
karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan kalimat: ")

hasil = f'{karakter} merupakan bagian dari "{kalimat}"' * (karakter in kalimat) or f'{karakter} tidak ditemukan dalam "{kalimat}"'

print(hasil)

#Konversi detik ke jam
print("Konversi detik ke jam")
detik = int(input("Masukkan jumlah detik:"))

jam = detik // 3600;
sisa_detik = detik % 3600;
menit = sisa_detik // 60;
detik = sisa_detik % 60

print(f"{jam:02d}:{menit:02d}:{detik:02d}")

#Konversi suhu
print ("Konversi Suhu dari Celcius ke kelvin, Reamur dan Fahrenheit")
celcius = int(input("Masukkan Suhu dalam Celcius: "))

kelvin =int(celcius + 273)
reamur = int(celcius * 0.8)
fahrenheit = int((celcius * 9/5) + 32)

print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Kelvin adalah : {kelvin}K")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Reamur adalah : {reamur}R")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Fahrenheit adalah : {fahrenheit}F")