def mulai():
    try:
        n = int(input("Masukkan bilangan bulat positif n: "))
        if n <= 0:
            print("Input tidak Valid")
            return
    except ValueError:
        print("Input tidak Valid")
        return

    step = 0
    print(f"n = {n}")
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
        step += 1
    print(f"Jumlah langkah: {step}")

mulai()