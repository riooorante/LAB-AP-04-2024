def akronim(kalimat):
    kata_kata = kalimat.split()
    akronim = ''.join(kata[0].upper() for kata in kata_kata)
    return akronim

kalimat = input("Masukkan kalimat: ")
print(":", akronim(kalimat))
