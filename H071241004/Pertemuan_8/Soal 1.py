import re

def check(kalimat): 
    # if len(kalimat) < 45:
    #     print("False")
    #     return
    
    karakter = r'^[a-zA-Z02468]{0,40}[13579\s]{5}$'

    if re.match(karakter, kalimat):
        print("True")
    else:
        print("False")

kalimat = input("Masukkan apa yang ingin dimasukkan : ")
check(kalimat)