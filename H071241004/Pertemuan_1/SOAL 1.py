#Rekomendasi Saham
harga_hari_ini = 105.0
harga_kemarin = float(input('Masukkan harga saham kemarin : '))
rumus = (harga_hari_ini - harga_kemarin) / harga_kemarin * 100
d = 'Beli' * (rumus > 5) + 'Tahan' * (5 >= rumus >= -3) + 'Jual' * (rumus < -3)
print(f'Perubahan persentase harga saham : {rumus :.2f}%')
print(f'Rekomendasi investasi : {d}')
