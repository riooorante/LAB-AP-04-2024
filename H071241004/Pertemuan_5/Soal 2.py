def acronym(s):
    words = s.split('=') #split dalam python membantu memisahkan kalimat dalam daftar
    print(words)
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

print(acronym("negara=republik")) 