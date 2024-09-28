#Konversi suhu
print ("Konversi Suhu dari Celcius ke kelvin, Reamur dan Fahrenheit")
celcius = int(input("Masukkan Suhu dalam Celcius: "))

kelvin =int(celcius + 273)
reamur = int(celcius * 0.8)
fahrenheit = int((celcius * 9/5) + 32)

print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Kelvin adalah : {kelvin}K")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Reamur adalah : {reamur}R")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Fahrenheit adalah : {fahrenheit}F")