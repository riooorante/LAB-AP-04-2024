import re

ipv4Pattern = r'^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
ipv6Pattern = r'^([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4})$'

hasil = []

def check_ip(ip_address):

    if re.match(ipv4Pattern, ip_address):
        return "IPv4"

    elif re.match(ipv6Pattern, ip_address):
        return "IPv6"
    else:
        return "Bukan IP Address"

ip_input = input("Masukkan alamat IP: ")
result = check_ip(ip_input)

print(result)