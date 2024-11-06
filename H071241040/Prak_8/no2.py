import re
def checkIP(addres):
    pattern4 = r"^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
    pattern6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    if re.match(pattern4, addres):
        return "IPv4"
    elif re.match(pattern6, addres):
        return "IPv6"
    return "Bukan IP Address"
a = int(input("Masukkan jumlah input: "))
for i in range(a):
    addres = input("Masukkan IP address: ")
    result = checkIP(addres)   
    print(result)
