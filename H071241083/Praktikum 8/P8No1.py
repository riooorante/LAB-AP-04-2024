import re

def validasi_string(input_string):
    
    if len(input_string) != 45:
        return False

    karakter_pertama_40 = r'^[a-zA-Z02468]{40}$'
    
    if not re.match(karakter_pertama_40, input_string[:40]):
        return False
    
    karakter_terakhir_5 = r'^[13579\s]{5}$'
    
    if not re.match(karakter_terakhir_5, input_string[40:]):
        return False

    return True

input_user = input("Masukkan string yang ingin divalidasi: ")

if validasi_string(input_user):
    print("True")
else:
    print("False")