# str1 = input("input your string: ")
# print("===========================")
# def sub_string(str):
#     for i in str :
#         print(i)
#     for i in range(len(str)-1):  
#         print(str[i:i+2])
#     for i in range(len(str)-2): 
#         print(str[i:i+3]) 
#     print(str)
# sub_string(str1)

str1 = input("Input your string: ")
print("===========================")
def substrings(str):
    panjang = len(str)
    for i in range(1, panjang + 1 ):  
        for k in range(panjang - i + 1):  
            print(str[k:k + i])
substrings(str1)
