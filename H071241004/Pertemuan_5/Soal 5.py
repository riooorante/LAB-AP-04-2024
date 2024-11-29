abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def enkripsi(kata, langkah):
    hasil = ""
    for i in kata:
        if i.isalpha(): 
            index_lama = abjad.index(i.lower())  
            index_baru = (index_lama + langkah) % len(abjad)  
            abjad_baru = abjad[index_baru]  
            if i.isupper():  
                abjad_baru = abjad_baru.upper()
            hasil += abjad_baru  
        else:
            hasil += i  
    return hasil

kata = input("Masukkan String : ")
langkah = int(input("Masukkan jumlah pergeseran : "))
hasil = enkripsi(kata, langkah)

print("Text :",  kata)
print("Shift :", langkah)
print("Cipher:", hasil)  