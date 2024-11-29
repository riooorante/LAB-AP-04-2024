def palindrome(p: str):
    p = p.lower().replace(" ", "") 
    if p == p[::-1]:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

palindrome("Ibu Ratna Antar Ubi")
palindrome("Sistem Informasi 2024")