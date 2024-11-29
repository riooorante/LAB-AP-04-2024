def hitung_penghapusan(string1, string2):
    string1 = ''.join(filter(str.isalnum, string1))   #str.isalnum untuk mengabaikan string selain huruf dan angka
    string2 = ''.join(filter(str.isalnum, string2))

    penghapusan = 0
    string = set(string1).union(set(string2))
    for karakter in string:
        penghapusan += abs(string1.count(karakter) - string2.count(karakter))

    return penghapusan

#meminta input user
string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")
hasil = hitung_penghapusan(string1, string2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hasil}")