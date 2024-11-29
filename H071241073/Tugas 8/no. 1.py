import re

def cek_validasi(string):
    
    pattern = r"^([A-Za-z02468]+){0,40}([13579\s]+){5}$"

    hasil =  re.match(pattern, string)
    if hasil:
        return True
    else:
        return False

str = input("Masukkan string: ")
print(cek_validasi(str))