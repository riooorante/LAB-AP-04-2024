

n = int(input("Masukkan jumlah baris: "))
m = int(input("Masukkan jumlah kolom:"))

for i in range(n):
    if  i%2 == 0:
        for j in range(m):
            print("MOVE to (",i,",",j,")",sep="")

    else:
        for j in range(m-1,-1,-1):
            print("MOVE to (",i,",",j,")",sep="")