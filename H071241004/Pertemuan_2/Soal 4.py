a = int(input("Masukkan jumlah data yang digunakan (GB): "))
b = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? : ")
c = input("Apakah Anda pengguna Personal atau Bisnis? : ")

if a < 10 and b == 'off-peak' and c == 'personal':
    paket = 'Paket A'
elif a <= 50 and b == 'peak' and c == 'personal':
    paket = 'Paket B'
elif a > 50 and b == 'peak' and c == 'personal':
    paket = 'Paket C'
elif a > 50 and b == 'off-peak' and c == 'bisnis':
    paket = 'Paket D'
else:
    paket = "Tidak ada paket yang cocok"

print(f"Paket yang sesuai: {paket}")