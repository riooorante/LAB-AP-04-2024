def minimum_penghapusan(string1, string2):
    
    frekuensi1 = {}
    frekuensi2 = {}

    
    for huruf in string1:
        if huruf.isalpha():  
            if huruf in frekuensi1:
                frekuensi1[huruf] += 1
            else:
                frekuensi1[huruf] = 1

    
    for huruf in string2:
        if huruf.isalpha(): 
            if huruf in frekuensi2:
                frekuensi2[huruf] += 1
            else:
                frekuensi2[huruf] = 1


    total_penghapusan = 0

    # Periksa string1
    for huruf in frekuensi1:
        if huruf in frekuensi2:
            total_penghapusan += abs(frekuensi1[huruf] - frekuensi2[huruf])
        else:
            total_penghapusan += frekuensi1[huruf]

    # Periksa string2
    for huruf in frekuensi2:
        if huruf not in frekuensi1:
            total_penghapusan += frekuensi2[huruf]

    return total_penghapusan


string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")


hasil = minimum_penghapusan(string1, string2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hasil}")