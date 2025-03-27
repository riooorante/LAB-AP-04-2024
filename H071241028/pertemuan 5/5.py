def caesar_cipher(teks, pergeseran):
    hasil = ""

    for char in teks:
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf
            shift = pergeseran % 26  # Menggunakan modulo 26 untuk menghindari pergeseran berlebih
            if char.islower():  # Jika huruf kecil
                # Menggeser dan mengatur ulang jika melampaui 'z'
                hasil += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():  # Jika huruf besar
                # Menggeser dan mengatur ulang jika melampaui 'Z'
                hasil += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Karakter lain (angka dan spesial) tetap tidak berubah
            hasil += char

    return hasil

# Mengambil input dari pengguna
input_string = input("Masukkan string: ")
shift_value = int(input("Masukkan jumlah pergeseran: "))

# Melakukan enkripsi
encrypted_string = caesar_cipher(input_string, shift_value)

# Menampilkan hasil
print(f"Text: {input_string}")
print(f"Shift: {shift_value}")
print(f"Cipher: {encrypted_string}")
