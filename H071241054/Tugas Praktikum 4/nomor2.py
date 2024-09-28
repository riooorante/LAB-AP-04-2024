total_jarak = 0
def hitung_total_jarak(langkah):
    global total_jarak
    total_jarak += langkah

def mencari_harta_karun():
    bahaya = False
    
    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))

            if langkah < 0:
                print("Input tidak valid. Harap masukkan bilangan bulat positif!")
                continue
            if langkah == 0:
                break
            if langkah > 20:
                bahaya = True
                print("Hati-hati langkah berbahaya!")

            hitung_total_jarak(langkah)

        except ValueError:
            print("Input tidak valid. Harap masukkan bilangan bulat positif!")

    print(f"Total jarak: {total_jarak}")

def ada_bahaya_keputusan(total_jarak):
    mencari_harta_karun()
    if total_jarak == 50:
        print("Ada bahaya: Tidak")
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        if total_jarak < 50:
            print("Ada bahaya: Ya")
            print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
        else:
            print("Ada bahaya: Ya")
            print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")

ada_bahaya_keputusan(total_jarak)