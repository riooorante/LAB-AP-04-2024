#mendefinisikan ukuran grid
N = int(input("Masukkan jumlah baris (N): "))
M = int(input("Masukkan jumlah kolom (M): "))

#mengontrol pergerakan robot
for i in range(abs(N)):
    if i % 2 == 0:
        for j in range(abs(M)):
            print(f"MOVE to ({i if N >= 0 else -i}, {j if M >= 0 else -j})")
    else:
        for j in range(abs(M)-1, -1, -1):
            print(f"MOVE to ({i if N >= 0 else -i}, {j if M >= 0 else -j})")