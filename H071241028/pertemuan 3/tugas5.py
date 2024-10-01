try:
    populasi_a = int(input("Masukkan populasi awal serangga A: "))
    populasi_b = int(input("Masukkan populasi awal serangga B: "))
    jumlah_hari = int(input("Masukkan jumlah hari: "))

    # Cek jika kedua populasi sudah habis sebelum memulai perhitungan
    if populasi_a <= 0 and populasi_b <= 0:
        print("Kedua populasi serangga telah habis.")
    else:
        for hari in range(1, jumlah_hari + 1):
            # Cek dan eksekusi perhitungan hanya jika populasi masih ada
            if populasi_a > 0:
                if hari % 2 != 0:  
                    populasi_a = int(populasi_a * 1.3)  
                else:  
                    populasi_a = int(populasi_a * 0.8) 

            if populasi_b > 0:
                if hari % 2 != 0:  
                    populasi_b = int(populasi_b * 1.5)  
                else:  
                    populasi_b = int(populasi_b * 0.6) 

            if hari % 5 == 0:
                print(f"Hari {hari}: Predator memakan 10% populasi.")
                if populasi_a > 0:
                    populasi_a = int(populasi_a * 0.9)  
                if populasi_b > 0:
                    populasi_b = int(populasi_b * 0.9)

            if populasi_a < 1 and populasi_b < 1:
                exit()
            else:
                print(f"Hari {hari}: Serangga A {f"= {populasi_a}" if populasi_a > 1 else "Telah habis"}, serangga B {f"= {populasi_b}" if populasi_b > 1 else "Telah habis"}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka yang benar.")