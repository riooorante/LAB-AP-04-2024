N = int(input("Masukkan jumlah baris (N): "))
M = int(input("Masukkan jumlah kolom (M): "))

for row in range(abs(N)):
    if row % 2 == 0:
        for col in range(abs(M)):
            print(f"MOVE to ({row if N >= 0 else -row}, {col if M >= 0 else -col})")
    else:
        for col in range(abs(M) - 1, -1, -1):
            print(f"MOVE to ({row if N >= 0 else -row}, {col if M >= 0 else -col})")
