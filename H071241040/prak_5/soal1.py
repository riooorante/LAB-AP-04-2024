def palindrom(a):
    revers = "".join(a.lower().split())
    if revers == revers[::-1]:
        print("palindrome")
    else :
        print("Not Palindrom")

palindrom("ibu Ratna antar ubi")



    