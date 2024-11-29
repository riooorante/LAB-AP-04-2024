def enkripsi_chiper(string, pergeseran):
    hasil_enkripsi = " "

    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in string:
        if char in huruf_kecil:
            posisi_awal = huruf_kecil.find(char)
            posisi_akhir = (posisi_awal + pergeseran) % 26
            hasil_enkripsi += huruf_kecil[posisi_akhir]
        elif char in huruf_besar:
            posisi_awal = huruf_besar.find(char)
            posisi_akhir = (posisi_awal + pergeseran) % 26
            hasil_enkripsi += huruf_besar[posisi_akhir]
        else:
            hasil_enkripsi += char

    return hasil_enkripsi

#meminta input user
string = input("Masukkan string: ")
pergeseran = int(input("Masukkan jumlah pergeseran: "))
chiper = enkripsi_chiper(string, pergeseran)
print(f"Chiper: {chiper}")