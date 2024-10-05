def acronym(default):
    pisah = default.split()
    ambil = [word[0] for word in pisah]
    print("".join(ambil))
acronym("Negara Kesatuan Republik Indonesia")

