def caesar_cipher(text, shift):
    hasil = ""  
    
    for huruf in text:
        
        if 'a' <= huruf <= 'z':
            geser = (ord(huruf) - ord('a') + shift) % 26 + ord('a')
            hasil += chr(geser)
        
        elif 'A' <= huruf <= 'Z':
            geser = (ord(huruf) - ord('A') + shift) % 26 + ord('A')
            hasil += chr(geser)
        
        else:
            continue
    
    return hasil

text = input("Masukkan string: ")  
shift = int(input("Masukkan jumlah pergeseran: "))  


print("\nText:", text)  
print("Shift:", shift)  
print("Cipher:", caesar_cipher(text, shift))  