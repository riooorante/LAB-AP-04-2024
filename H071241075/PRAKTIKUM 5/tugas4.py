def caesar_cipher(teks: str, pergeseran: int) -> str:
    hasil = ""

    for karakter in teks:

        if karakter.islower():

            hasil += chr((ord(karakter) - ord('a') + pergeseran) % 26 + ord('a'))

        elif karakter.isupper():

            hasil += chr((ord(karakter) - ord('A') + pergeseran) % 26 + ord('A'))

        else:
            hasil += karakter

    return hasil


input_teks = input("Masukkan string untuk dienkripsi: ")
input_pergeseran = int(input("Masukkan jumlah pergeseran (integer positif): "))


hasil_enkripsi = caesar_cipher(input_teks, input_pergeseran)

print("Hasil enkripsi:", hasil_enkripsi)

