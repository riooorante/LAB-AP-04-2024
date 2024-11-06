def chiper(string, shift):
    hasil = []
    for i in string:
        if i.isalpha():
            batas = "a" if i.islower() else "A"
            hasil.append(chr((ord(i) - ord(batas) - shift) % 26 + ord(batas)))
        else:
            hasil.append(i)
    return ''.join(hasil)
string = input("Masukkan string: ")
shift = int(input("Masukkan jumlah pergeseran: "))
print(f"Text: {string}")
print(f"shift: {shift}")
print(f"Chipper:", chiper(string, shift))

#ASCII "a" = 97, "A"=65
# (97-97 +1 % 26)+97= 98
