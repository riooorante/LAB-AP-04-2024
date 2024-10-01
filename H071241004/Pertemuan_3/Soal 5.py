while True:
    try:
        seranggaA = int(input("Masukkan Populasi Awal Serangga A: "))
        if seranggaA <= 0:
            print("Populasi awal serangga tidak boleh 0 atau di bawah 0")
        else:
              break
    except ValueError:
          print("Input harus dalam bentuk angka")

while True:
    try:
        seranggaB = int(input("Masukkan Populasi Awal Serangga B: "))
        if seranggaB <= 0:
            print("Populasi awal serangga tidak boleh 0 atau di bawah 0")
        else:
             break
    except ValueError:
         print("Inputan harus dalam bentuk angka")
    
while True:
    try:
        jumlah_hari = int(input("Masukkan jumlah hari : "))
        if jumlah_hari <= 0:
            print("Jumlah hari tidak boleh 0 atau di bawah 0")
        else:
             break
    except ValueError:
         print("Inputan harus dalam bentuk angka")

for i in range(1, jumlah_hari + 1):
    if i % 2 != 0:  # Hari ganjil
            seranggaA += seranggaA * 0.3  # Bertambah 30%
            seranggaB += seranggaB * 0.5  # Bertambah 50%
    elif i % 2 == 0:  # Hari genap
            seranggaA -= seranggaA * 0.2  # Berkurang 20%
            seranggaB -= seranggaB * 0.4  # Berkurang 40%

    if i % 5 == 0:
          print("Predator memakan 10% populasi.")
          seranggaA -= seranggaA * 0.1 + 1 # Berkurang 10%
          seranggaB -= seranggaB * 0.1 + 1 # Berkurang 10%
    
    a = f"= {seranggaA:.0f}" if seranggaA > 0 else 'telah habis'
    b = f"= {seranggaB:.0f}" if seranggaB > 0 else 'telah habis'
   
    print(f"Hari {i}: Serangga A {a}, Serangga B {b}")
    if a == 'telah habis' and b == 'telah habis':
        break