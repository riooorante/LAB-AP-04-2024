def buat_akronim(kalimat):
    kata_kata = kalimat.split('=')

    akronim = ''
    for kata in kata_kata:
        akronim += kata[0].upper()

    return akronim

kalimat = input("Kalimat: ")

print("Akronim:", buat_akronim(kalimat))