n = int(input("N = ")) # nilai x
m = int(input("M = ")) # nilai y

for i in range(abs(n)):
    if i%2 == 0:
        for j in range(abs(m)):
            print(f"MOVE to ({i if n >= 0 else -i }),({j if m >= 0 else -j})") 
    else:
        for j in range (abs(m)-1,-1,-1):
            print(f"MOVE to ({i if n >= 0 else -i}),({j if m >= 0 else -j})")



    