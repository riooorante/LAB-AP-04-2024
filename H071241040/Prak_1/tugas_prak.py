#Nomor 1
hari_ini = 105.0
kemarin = float(input("Masukkan harga saham kemarin : "))
output = ["jual","Tahan","Beli"]
persen_baru = ((hari_ini-kemarin)/kemarin)*100
hasil = output [(persen_baru > -3)+(persen_baru > 5)]
print(f"perubahan persentasi harga saham {persen_baru}%")
print(hasil)

# hari_ini = 105.0
# kemarin = float(input("Masukkan harga saham kemarin : "))
# output = ["jual","Tahan","Beli"]
# persen_baru = ((hari_ini-kemarin)/kemarin)*100
# if persen_baru > 5:
#     print("beli")
# elif -3< persen_baru <= 5 :
#     print("tahan")
# else :
#     print("jual")

#Nomor 2
karakter = input("Masukkan Karakter :")
kalimat = input("Kalimat : ")
output = ["tidak ditemukan","ditemukan"] 
hasil = output[(karakter in kalimat)]
print(f'{karakter} {hasil} dalam "{kalimat}" ')

#Nomor 3
print("Konfersi Detik Ke Jam")
detik = int(input("Masukkan Jumlah Detik : "))
jam = int(detik//3600)
menit =int(detik-(jam*3600))//60
detik = (detik-(jam*3600)-(menit*60))
print(f"{jam:02}:{menit}:{detik}")
# #Nomor 4
print("Konversi Suhu dari Celcius ke Kelvin, Reamur, Fahrenheit")
celcius = float(input("Masukkan Suhu dalam Celcius :"))
kelvin = 273.15 + celcius
reamur = celcius * 4 / 5
fahrenheit = (9/5 * celcius)+32
template = (f"Hasil Konversi dari suhu {celcius} ke")
print(f"""{template} Kelvin adalah : {kelvin}K
{template} Reamur adalah : {reamur}R
{template} Fahrenheit adalah : {fahrenheit}F""")