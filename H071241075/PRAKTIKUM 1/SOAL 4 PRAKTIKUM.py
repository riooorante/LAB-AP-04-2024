print('Konversi suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit')


celcius = float(input('Masukkan suhu dalam Celcius: '))


kelvin = celcius + 273.15
reamur = (4/5) * celcius
fahrenheit = (9/5) * celcius + 32

print(f'Hasil konversi suhu dari {celcius:.1f} derajat Celcius ke Kelvin adalah : {kelvin:.2f} K')
print(f'Hasil konversi suhu dari {celcius:.1f} derajat Celcius ke Reamur adalah : {reamur:.2f} R')
print(f'Hasil konversi suhu dari {celcius:.1f} derajat Celcius ke Fahrenheit adalah : {fahrenheit:.2f} F')
