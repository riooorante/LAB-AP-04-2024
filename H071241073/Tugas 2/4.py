data = float(input("Masukkan jumlah data yang digunakan (GB): "))
waktu = input("Apakah mayoritas penggunaan diluar jam sibuk (off-peak) atau di jam sibuk (peak)? ").lower()
pengguna = input("Apakah anda pengguna Personal atau Bisnis? ").lower()

if data < 10 and waktu == "off-peak" and pengguna == "personal" :
    paket = "A"
elif 10 <= data <= 50 and waktu == "peak" and pengguna == "personal" :
    paket = "B"
elif data > 50 and waktu == "peak" and (pengguna == "personal" or pengguna == "bisnis") :
    paket = "C"
elif data > 50 and waktu == "off-peak" and pengguna == "bisnis" :
    paket = "D"
else :
    print("Tidak ada paket yang cocok")
    paket = None

if paket :
    print(f'Paket yang sesuai: Paket {paket}')