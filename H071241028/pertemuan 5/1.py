def palindrome(s):
    # Menghapus spasi dan mengubah ke huruf kecil
    cleaned_string = ''.join(s.split()).lower()
    
    # Memeriksa apakah string sama dengan kebalikannya
    if cleaned_string == cleaned_string[::-1]:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

# Contoh penggunaan
palindrome("ibu ratna antar ubi")  # Output: Palindrome
palindrome("Sistem Informasi Angkatan 2024")  # Output: Bukan Palindrome
