populasi_a = int(input("Masukkan populasi awal Serangga A: ")) 
populasi_b = int(input("Masukkan populasi awal Serangga B: ")) 
jumlah_hari = int(input("Masukkan jumlah hari: ")) 

for hari in range(1, jumlah_hari + 1): 
  if hari % 2 != 0:                      
    populasi_a = int(populasi_a * 1.3)   
    populasi_b = int(populasi_b * 1.5)    

  else:                                   
    populasi_a = int(populasi_a * 0.8)    
    populasi_b = int(populasi_b * 0.6)    

  if hari % 5 == 0:                       
    print(f"Hari {hari}: Predator memakan 10% populasi.") 
    populasi_a = int(populasi_a * 0.9)    
    populasi_b = int(populasi_b * 0.9)

  if populasi_a < 1 and populasi_b < 1 :
    exit()
  else:
    print(f"Hari {hari}: Serangga A {f"= {populasi_a}" if populasi_a > 1 else "Telah habis"}, Serangga B {f"= {populasi_b}" if populasi_b > 1 else "Telah habis"}  ")