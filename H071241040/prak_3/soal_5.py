a = int(input("Masukkan Populasi awall serangga A: "))
b = int(input("Masukkan Populasi awall serangga B: "))
hari = int(input("Masukkan Jumlah Hari : "))
for i in range (1, hari+1):
    if a > 0.9 and b > 0.9:
        if (i%5) == 0:  
            a = a*90//100
            b = b*90//100
            print(f"Hari {i}: Predator memakan 10% populasi")
            if (i%2) != 0:
                a = a*130//100
                b = b*150//100
                if a > 0 and b > 0:
                    print(f"Hari {i}:  Serangga A = {a}, Serangga B = {b}")
            elif (i%2) == 0:
                a = a*80//100
                b = b*60//100
                if a > 0 and b > 0:
                    print(f"Hari {i}:  Serangga A = {a}, Serangga B = {b}")
        elif (i%2) != 0:
            a = a*130//100
            b = b*150//100
            if a > 0 and b > 0:
                print(f"hari {i}:  Serangga A = {a}, Serangga B = {b}")
        elif (i%2) == 0:
            a = a*80//100
            b = b*60//100
            if a > 0 and b > 0:
                print(f"Hari {i}:  Serangga A = {a}, Serangga B = {b}")
    elif a < 1 and b > 0 :
        if (i%2) == 0:
            b = b*60//100
        elif (i%2) != 0 :
            b = b*150//100
            if b > 0 : 
                print(f"Hari {i}:  Serangga A = Telah Habis, Serangga B = {b}")      
    elif b < 1  and a > 0:
        if (i%2) == 0:
            a = a*80//100
            if a > 0:
                print(f"Hari {i}:  Serangga A = {a}, Serangga B = Telah habis")
        elif (i%2) != 0 :
            a = a*130//100
            if a > 0 :
                print(f"Hari {i}:  Serangga A = {a}, Serangga B = Telah habis")
        
    else :
        print(f"Hari {i}:  Serangga A = Telah habis, Serangga B = Telah habis")
        quit()
        
       
   
        