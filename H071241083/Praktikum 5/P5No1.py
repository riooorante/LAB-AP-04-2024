x = input(":")
y = reversed(x)

z ="".join(y)

if z == x:
    print("Palindrome")
else:
    print("Not Palindrome")