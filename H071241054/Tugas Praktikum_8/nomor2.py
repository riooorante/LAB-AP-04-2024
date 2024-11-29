#format IPv4: P.Q.R.S merupakan bilangan bulat dari 0 - 255
#IPv6 dipisahkan tanda :
import re
N = int(input("Masukkan jumlah baris inputan: "))

ip_adresses = []
for i in range(N):
    ip = input(f"Masukkan ip adress ke-{i+1} yang ingin dicek: ")

    if len(ip) > 500:
        print(f"Inputan ke-{i+1} melebihi 500 karakter. Silakan masukkan kembali.")
        continue

    ip_adresses.append(ip)

pattern_IPv4 = r"""
^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
"""
pattern_IPv4 = pattern_IPv4.replace('\n', '')

pattern_IPv6 = r"^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})$"

for ip in ip_adresses:
    cek_IPv4 = re.match(pattern_IPv4, ip)
    cek_IPv6 = re.match(pattern_IPv6, ip)

    if cek_IPv4:
        print("IPv4")
    elif cek_IPv6:
        print("IPv6")
    else:
        print("Bukan IP Adress")