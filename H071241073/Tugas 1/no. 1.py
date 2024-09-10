harga_saham_kemarin = int(input('Masukkan harga saham kemarin : '))
harga_saham_hari_ini = 105.0
perubahan_presentase = ((harga_saham_hari_ini - harga_saham_kemarin) / harga_saham_kemarin) * 100

rekomendasi = (
    ("Beli", perubahan_presentase > 5),
    ("Tahan", -3 <= perubahan_presentase <= 5),
    ("Jual", perubahan_presentase < -3)
)

hasil_rekomendasi = [r[0] for r in rekomendasi if r[1]][0]

print(f"Perubahan presentase harga saham : {perubahan_presentase:.2f}%")
print(f"Rekomendasi : {hasil_rekomendasi}")