def periksa_langkah(jarak):
    return jarak > 20

def permainan_harta_karun():
    total_jarak = 0
    bahaya_terdeteksi = False
    
    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            if langkah <= 0:
                break
            total_jarak += langkah

            if periksa_langkah(langkah):
                bahaya_terdeteksi = True
                print("Langkah ini berbahaya! Tidak aman untuk menggali harta karun.")
                
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    print(f"Total jarak: {total_jarak} meter")
    if total_jarak > 50 or bahaya_terdeteksi:
        print("Ada bahaya: Ya")
    else:
        print("Ada bahaya: Tidak")
        
    if total_jarak == 50 and not bahaya_terdeteksi:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    elif bahaya_terdeteksi:
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")
        
permainan_harta_karun()