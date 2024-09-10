def rekomendasi_investasi(persen_perubahan):
    rekomendasi_dict = {
        persen_perubahan > 5: "Beli",
        -3 <= persen_perubahan <= 5: "Tahan",
        persen_perubahan < -3: "Jual"
    }
    return rekomendasi_dict[True]

def hitung_persen_perubahan(harga_kemarin, harga_hari_ini):
    return ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

harga_hari_ini = 105.0

harga_kemarin = float(input("Masukkan harga saham kemarin: "))

persen_perubahan = hitung_persen_perubahan(harga_kemarin, harga_hari_ini)

rekomendasi = rekomendasi_investasi(persen_perubahan)

print(f"Perubahan persentase harga saham: {persen_perubahan:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi}")