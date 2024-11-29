import re

def check_ip_address(ip):
    ipv4 = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'

    ipv6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    #IPv4
    if re.match(ipv4, ip):
        return "IPv4"
    #IPv6
    elif re.match(ipv6, ip):
        return "IPv6"
    else:
        return "Bukan IP Address"

try:
    N = int(input("Masukkan jumlah baris: "))
    if N <= 0:
        print("Jumlah baris harus positif.")
    else:
        for _ in range(N):
            ip_input = input("Masukkan IP: ").strip()
            if len(ip_input) > 500:
                print("Bukan IP Address") 
            else:
                print(check_ip_address(ip_input))

except ValueError:
    print("Input tidak valid. Harap masukkan angka yang sesuai.")
