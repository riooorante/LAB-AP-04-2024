A = int(input("Masukkan jumlah data yang digunakan(dalam GB per bulan): "))
B = input("Apakah mayoritas penggunaan diluar jam sibuk(off-peak) atau di jam sibuk(peak): ")
C = input("Apakah anda pengguna personal atau bisnis: ")

if A < 10:
    if B == "off-peak" and C == "personal":
        paket = "Paket A"
    else:
        paket = "Tidak ada paket yang cocok"
elif 10 <= A <= 50:
    if B == "peak" and C == "personal":
        paket = "Paket B"
    else:
        paket = "Tidak ada yang cocok"
elif A > 50:
    if B == "peak":
        paket = "Paket C"
    elif B == "off-peak" and C == "bisnis":
        paket = "Paket D"
    else:
        paket = "Tidak ada yang cocok"
else:
    paket = "Tidak ada yang cocok"

print("Paket yang sesuai adalah: ", paket)