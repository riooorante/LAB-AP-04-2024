import re

def validasi_string(s):
    if len(s) != 45:
        return False
    
    pola_40_karakter_pertama = r'^[A-Za-z02468]{40}$'
    pola_5_karakter_terakhir = r'^[13579\s]{5}$'
    
    if not re.match(pola_40_karakter_pertama, s[:40]):
        return False
    
    if not re.match(pola_5_karakter_terakhir, s[40:]):
        return False
    
    return True

input_string = input("Masukkan string: ")
hasil = validasi_string(input_string)
print(hasil)