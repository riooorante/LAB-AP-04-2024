import re
from collections import Counter

def bersihkan_string(teks: str) -> str:
    return re.sub(r'[^a-zA-Z]', '', teks)

def hitung_penghapusan_minimum_anagram(string_pertama: str, string_kedua: str) -> int:

    string_pertama_bersih = bersihkan_string(string_pertama).lower()
    string_kedua_bersih = bersihkan_string(string_kedua).lower()
    print(string_pertama_bersih)
    print(string_kedua_bersih)

    hitung_karakter_pertama = Counter(string_pertama_bersih)
    hitung_karakter_kedua = Counter(string_kedua_bersih)


    penghapusan_dari_pertama = sum((hitung_karakter_pertama - hitung_karakter_kedua).values())
    penghapusan_dari_kedua = sum((hitung_karakter_kedua - hitung_karakter_pertama).values())


    total_penghapusan = penghapusan_dari_pertama + penghapusan_dari_kedua

    return total_penghapusan


input_string_pertama = input("Masukkan string pertama: ")
input_string_kedua = input("Masukkan string kedua: ")

jumlah_penghapusan = hitung_penghapusan_minimum_anagram(input_string_pertama, input_string_kedua)
print(f"Jumlah minimum penghapusan karakter untuk membuat anagram: {jumlah_penghapusan}")
