#Memvalidasi string inputan
import re

my_string = str(input("Masukkan string: "))

pattern = r"^([A-Za-z02468]+){0,40}([13579\s]+){5}$"
hasil_periksa = re.match(pattern, my_string)

if not hasil_periksa:
    print("False")
else:
    print("True")