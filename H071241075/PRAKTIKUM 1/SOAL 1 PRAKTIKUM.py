SahamHariIni = 105.0
SahamKemarin = float(input("Masukkan harga saham kemarin : "))

perubahanPersentase = ((SahamHariIni - SahamKemarin) / SahamHariIni) * 100

rekomendasiDict = {
    "Beli": perubahanPersentase > 5,
    "Tahan": perubahanPersentase < 5 and perubahanPersentase > -3,
    "Jual": perubahanPersentase < -3,
}

for temp in rekomendasiDict:
    if rekomendasiDict[temp]:
        rekomendasi = temp
        break

print(f"Rekomendasi investasi: {rekomendasi}")