celcius = int(input("Masukkan suhu dalam celcius : "))

kelvin = celcius + 273.15
reamur = celcius * 0.8
fahrenheit = (celcius * 1.8) + 32

print(
    f"Hasil konversi dari suhu {celcius} derajat Celsius ke Kelvin : {kelvin:.0f}K\n"
    f"Hasil konversi dari suhu {celcius} derajat Celsius ke Reamur adalah : {reamur:.0f}R\n"
    f"Hasil konversi dari suhu {celcius} derajat Celsius ke Fahrenheit adalah : {fahrenheit:.0f}F"
)