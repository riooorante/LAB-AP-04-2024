import re
def ValidasiString(string):
    pattern = r"^(?=.*[a-zA-Z02468])[a-zA-Z02468]{1,40}[13579\s]{5}$"
    return re.search(pattern, string)
input = input("Masukkan string (45 karakter): ")
# if len(input) != 45:
#     print("angka yang anda masukkan bukan 45 karakter")
#     quit()
if ValidasiString(input):
    print("True")
else:
    print("False")

