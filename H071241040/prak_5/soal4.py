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
#outputnya
# loop 1 = [0:0+1] M
# loop 1 = [1:1+1] I
# loop 1 = [2:2+1] P
# loop 1 = [3:3+1] A
 
# loop 2 = [0:0+2] MI
# loop 2 = [1:1+2] IP
# loop 2 = [2:2+2] PA -> 2-3 atau mulai dari 2 sampai sebelum 4

#loop 3 = [0:0+3] MIP
#loop 3 = [1:1+3] IPA

#loop 4 = [0:0+4] MIPA

