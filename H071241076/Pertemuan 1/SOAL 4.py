print('Konfersi Suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit')
suhu_celcius = float(input("Masukkan suhu dalam Celcius: "))

# Konversi suhu
suhu_kelvin = suhu_celcius + 273.15
suhu_reamur = suhu_celcius * 4/5
suhu_fahrenheit = suhu_celcius * 9/5 + 32

# Hasil konversi
print(f"Suhu dalam Kelvin    : {suhu_kelvin:.2f} K")
print(f"Suhu dalam Reamur    : {suhu_reamur:.2f} °Re")
print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit:.2f} °F")