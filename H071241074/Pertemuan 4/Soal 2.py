def minta_langkah():
    try:
        langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
        return langkah 
    except ValueError:
        print("Input tidak valid. Masukkan bilangan bulat.")
        return None 

def hitung_jarak(total_jarak, langkah):
    if langkah < 0:
        print("Input tidak valid. Masukkan bilangan bulat positif.")
        return total_jarak, False
    total_jarak += langkah  
    bahaya = langkah > 20 
    return total_jarak, bahaya  

def tampilkan_hasil(total_jarak, bahaya):
    print(f"Total jarak: {total_jarak} meter") 

    if bahaya:
        print("Ada bahaya: Ya")
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_jarak == 50:
        print("Ada bahaya: Tidak")
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    elif total_jarak < 50:
        print("Ada bahaya: Tidak")
        print("Tidak ada harta. Coba jalan lagi!")
    else:
        print("Ada bahaya: Tidak")
        print("Tidak ada. Coba lagi!")


total_jarak = 0 
bahaya = False 

while True:
    langkah = minta_langkah()  

    if langkah == 0:
        break

    total_jarak, ada_bahaya = hitung_jarak(total_jarak, langkah)
    
    if ada_bahaya:
        bahaya = True

tampilkan_hasil(total_jarak, bahaya)