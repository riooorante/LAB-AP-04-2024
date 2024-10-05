def acronym(frasa):
    kata2 = frasa.split()

    akronim = ''.join(kata[0].upper() for kata in kata2)

    return akronim

hasil = acronym("partai komunis indonesia")
hasil2 = acronym("Negara=Kesatuan=Republik=Indonesia")
print(hasil)
print(hasil2)

