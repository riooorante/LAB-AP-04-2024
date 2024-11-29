def palindrome(s: str) -> str:
    s = s.lower()
    if  s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome("Ibu Ratna Antar Ubi")
palindrome("Sistem Informasi 2024")