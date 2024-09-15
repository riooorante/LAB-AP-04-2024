inputan1 = input("Masukkan inputan pertama : ")

if inputan1 == "vertebrado":
    inputan2 = input("Masukkan inputan kedua : ")
    if inputan2 == "ave":
        inputan3 = input("Masukkan inputan ketiga: ")
        if inputan3 == "carnivoro":
            print("aguia")
        elif inputan3 == "onivoro":
            print("pomba")
        else:
            print("Inputan yang dimasukkan salah")
    elif inputan2 == "mamifero":
        inputan4 = input("Masukkan inputan ketiga : ")
        if inputan4 == "onivoro":
            print("homem")
        elif inputan4 == "herbivoro":
            print("vaca")
        else:
                print("Inputan yang dimasukkan salah")
    else:
        print("Inputan yang dimasukkan salah")
elif inputan1 == "invertebrado":
    keluar = input("Masukkan inputan kedua : ")
    if keluar == "inseto":
        keluar2 = input("Masukkan inputan ketiga : ")
        if keluar2 == "hematofago":
            print("pulga")
        elif keluar2 == "herbivoro":
            print("lagarta")
        else:
            print("Inputan yang dimasukkan salah")
    elif keluar == "anelideo":
        keluar3 = input("Masukkan inputan ketiga : ")
        if keluar3 == "hematofago":
            print("sanguessuga")
        elif keluar3 == "onivoro":
            print("minhoca")
        else:
            print("Inputan yang dimasukkan salah")
    else:
        print("Inputan yang dimasukkan salah")
else:
    print("Inputan yang dimasukkan salah")