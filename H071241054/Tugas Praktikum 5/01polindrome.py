def palindrome(string):
    palindrom = "".join(reversed(string))
    if string == palindrom:
        print("Palindrome")
    else:
        print("Not Palindrome")  
    

#meminta input user
string = input("Masukkan kata/kalimat: ").lower()
palindrome(string)