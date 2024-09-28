def input_distance():
    """Fungsi untuk mengambil input jarak langkah dari pemain."""
    while True:
        try:
            distance = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            return distance
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

def treasure_hunt():
    """Fungsi utama untuk menjalankan permainan berburu harta karun."""
    total_distance = 0
    danger_detected = False
    
    while True:
        distance = input_distance()
        
        if distance < 0:
            print("Langkah tidak dapat negatif. Permainan dihentikan.")
            break
        elif distance == 0:
            break
        
        total_distance += distance
        
        if distance > 20:
            danger_detected = True
    
    print(f"Total jarak: {total_distance} meter")
    if danger_detected:
        print("Ada bahaya: Ya")
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        if total_distance == 50:
            print("Aman! Kamu tepat menemukan harta karun dan menang!")
        else:
            print("Tidak menemukan harta karun. Coba lagi!")

# Memulai permainan
treasure_hunt()
