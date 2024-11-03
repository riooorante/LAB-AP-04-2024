import re

def validasi_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$"
    return re.search(pattern, username)

def validasi_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9.-]+\.(ac\.id|com|co\.id)$"
    return re.search(pattern, email)

def validasi_password(password):
    pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return re.search(pattern, password)

username = input("Masukkan username : ")

if validasi_username(username):
    email = input("Masukkan email : ")
    
    if validasi_email(email):
        password = input("Masukkan password : ")
        
        if validasi_password(password):
            print(f"\nRegistrasi berhasil! Halo {username}") 
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
            
    else:
        print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
        
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")