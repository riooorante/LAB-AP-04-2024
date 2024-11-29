def semua_substring(teks: str):
    panjang = len(teks)

    # Menghasilkan semua substring
    for i in range(panjang):
        for j in range(i + 1, panjang + 1):
            # Mengambil substring dari indeks i hingga j
            substring = teks[i:j]
            print(substring)

# Menerima input dari pengguna
input_teks = input("Masukkan string: ")

# Menampilkan semua substring
semua_substring(input_teks)
