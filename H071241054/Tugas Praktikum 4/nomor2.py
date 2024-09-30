total_jarak = 0
def hitung_total_jarak(langkah):
    global total_jarak
    total_jarak += langkah

def ada_bahaya(total_jarak):
    if total_jarak == 50:
        bahaya = "Tidak"
    elif total_jarak < 50:
        bahaya = "-"
    else:
        bahaya = "Ya"
    return bahaya

def keputusan_akhir(total_jarak):
    if total_jarak == 50:
        keputusan = "Aman! Kamu tepat menemukan harta karun dan menang!"
    elif total_jarak < 50:
        keputusan = "Tidak menemukan harta karun. Coba lagi!"
    else:
        keputusan = "Tidak aman untuk menggali harta karun. Coba lagi!"
    return keputusan

while True:
    try:
        langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: ")) #meminta input dari pengguna

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
print(f"Ada bahaya: {ada_bahaya(total_jarak)}")
print(f"Keputusan: {keputusan_akhir(total_jarak)}")