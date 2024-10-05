def palindrome(polindrom):
    huruf = ''.join(polindrom.lower())
    # if huruf == huruf[::-1]:
    #     print("Palindrome")
    # else:
    #     print("Not Palindrome")

    if huruf == ''.join(reversed(huruf)):
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome("Ibu Ratna Antar Ubi")
palindrome("Sistem Informasi 2024")