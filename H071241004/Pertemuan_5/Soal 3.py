def anagram(str1, str2):
    char_count = {}
    
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
    
    deletions = 0
    for count in char_count.values():
        deletions += abs(count)
    
    return deletions

str1 = input("Masukkan string pertama : ")
str2 = input("Masukkan string 2\kedua : ")
hasil =  anagram(str1, str2)
print("Jumlah minimum penghapusan untuk membuat anagram:" ,hasil)