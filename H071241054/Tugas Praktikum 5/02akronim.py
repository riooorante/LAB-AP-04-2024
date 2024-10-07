def akronim(string):
    akronim = " "
    panjang = len(string)
    for i in range(panjang):
        #ambil huruf pertama dari setiap kata
        if (i == 0 or string[i - 1] == ' ') and string[i] != " ":
            akronim += string[i].upper()
    return akronim

#meminta input user
string = input("Masukkan string: ")
akro = akronim(string)
print(f"Akronim: {akro}")