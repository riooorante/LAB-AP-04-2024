#nomor 4
#input dari pengguna
penggunaan_data = int(input("Masukkan jumlah data yang digunakan (GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)?: ")
jenis_pengguna = input("Apakah anda pengguna personal atau bisnis?: ")

if jenis_pengguna == "personal":
    if penggunaan_data < 10 and waktu_penggunaan == "off-peak":
        print("Paket yang sesuai: Paket A")
    elif 10<= penggunaan_data <= 50 and waktu_penggunaan == "peak":
        print("Paket yang sesuai: Paket B")
    elif penggunaan_data > 50 and waktu_penggunaan == "peak":
        print("Paket yang sesuai: Paket C")
    else:
        print("Tidak ada paket yang cocok")
        
elif jenis_pengguna == "bisnis":
    if penggunaan_data > 50 and waktu_penggunaan == "peak":
        print("Paket yang sesuai: Paket C")
    elif penggunaan_data > 50 and waktu_penggunaan == "off-peak":
        print("Paket yang sesuai: Paket D")    
    else:
        print("Tidak ada paket yang cocok")
else:
    print("Tidak ada paket yang cocok")