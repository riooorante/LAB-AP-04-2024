kata = input("Input your string : ")
print('=' * 20)

for i in range(1, len(kata) + 1):
    for j in range(len(kata) - i + 1):
        substring = kata[j:j + i] 
        print(substring)