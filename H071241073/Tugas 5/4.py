x = input("Input your string: ")
y = "="
yy = y *25
print(yy)

n = len(x)
subx = []

for i in range(n):
    for j in range(i + 1, n + 1):
        subx.append(x[i:j])
subx.sort(key=len)
print(subx)

for subxs in subx:
    print(subxs)