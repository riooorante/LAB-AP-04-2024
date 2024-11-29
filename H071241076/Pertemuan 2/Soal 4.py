# Input data
data_gb = int(input("Masukkan jumlah data yang digunakan (GB): "))


if data_gb<0:
    print("jumlah data tidak valid")
# Kategori
else:
    waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ").lower()
    jenis_pengguna = input("Apakah Anda pengguna Personal atau Bisnis? ").lower()
    if data_gb < 10:
        penggunaan = "ringan"
    elif 10<=data_gb<= 50:
        penggunaan = "sedang"
    else:
        penggunaan = "berat"

# Rekomendasi
    if penggunaan == "ringan" and waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
        print("Paket yang sesuai: Paket A")
    elif penggunaan == "sedang" and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
        print("Paket yang sesuai: Paket B")
    elif penggunaan == "berat"  and waktu_penggunaan == "peak" and (jenis_pengguna == "personal" or jenis_pengguna == "bisnis"):
        print("Paket yang sesuai: Paket C")
    elif penggunaan == "berat" and waktu_penggunaan == "off-peak" and jenis_pengguna == "bisnis":
        print("Paket yang sesuai: Paket D")
    else:
        print("Tidak ada paket yang cocok untuk profil Anda.")