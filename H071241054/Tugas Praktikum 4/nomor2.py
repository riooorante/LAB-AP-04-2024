total_jarak = 0
def hitung_total_jarak(langkah):
    global total_jarak
    total_jarak += langkah

def ada_bahaya_keputusan(total_jarak):
    if total_jarak == 50:
        bahaya = "Tidak"
        keputusan = "Aman! Kamu tepat menemukan harta karun dan menang!"
    elif total_jarak < 50:
        bahaya = "-"
        keputusan = "Tidak menemukan harta karun. Coba lagi!"
    else:
        bahaya = "Ya"
        keputusan = "Tidak aman untuk menggali harta karun. Coba lagi!"

    print(f"Ada bahaya: {bahaya}")
    print(f"Keputusan: {keputusan}")

while True:
    try:
        langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))

        if langkah < 0:
            print("Input tidak valid. Harap masukkan bilangan bulat positif!")
            continue
        if langkah == 0:
            break
        if langkah > 20:
            print("Hati-hati langkah anda berbahaya!")

        hitung_total_jarak(langkah)

    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat positif!")
    
print(f"Total jarak: {total_jarak} meter")
ada_bahaya_keputusan(total_jarak)