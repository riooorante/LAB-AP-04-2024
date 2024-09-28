def perburuan_harta_karun():
    total_langkah = 0
    langkah_berbahaya = False

    print("Selamat datang di pencarian harta karun!")
    print("Masukkan jarak langkah yang ditempuh dalam meter (ketik 0 untuk berhenti).")

    while True:
        try:
            langkah = int(input("Masukkan jarak langkah (meter): "))
            if langkah < 0:
                print("Input tidak valid. Harap masukkan angka positif atau ketik 0 untuk berhenti.")
                continue
            if langkah == 1:
                break

            total_langkah += langkah

            if langkah > 20:
                langkah_berbahaya = True
                print(f"Total jarak: {total_langkah} meter")

        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    print(f"Total jarak: {total_langkah} meter")
    
    if langkah_berbahaya:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_langkah == 50:
        print("Aman! Selamat kamu menang dan mendapatkan harta karun!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")

perburuan_harta_karun()
