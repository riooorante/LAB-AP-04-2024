#Input suhu dari celcius
Celcius = float(input("Masukkan suhu dalam celcius: "))

#Menghitung konversi suhu
Kelvin = Celcius + 273.15             #konversi ke kelvin
Reamur = (4/5)*Celcius                #konversi ke reamur
Fahrenheit = ((9/5)*Celcius)+32       #konversi ke fahrenheit

#Hasil konversi
print(f"Hasil konversi dari suhu {Celcius} derajat celcius ke kelvin adalah: {Kelvin}K")
print(f"Hasil konversi dari suhu {Celcius} derajat celcius ke reamur adalah: {Reamur}R")
print(f"Hasil konversi dari suhu {Celcius} derajat celcius ke kelvin adalah: {Fahrenheit}F")