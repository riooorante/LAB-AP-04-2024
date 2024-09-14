#nomor 3
#input dari penggunaan
nilai_akhir = int(input("Masukkan nilai akhir: "))

if 0<= nilai_akhir <= 100:
  kehadiran = int(input("Masukkan persentase kehadiran: "))
  if kehadiran < 75:
    print("Tidak lulus")
  elif kehadiran >= 75:
    if 85<= nilai_akhir <= 100:
      print("Lulus dengan predikat A")
    elif 70<= nilai_akhir <= 84:
      print("Lulus dengan predikat B")
    elif 60<= nilai_akhir <= 69:
      print("Lulus dengan predikat C")
    else:
      tugas_tambahan = int(input("Masukkan nilai rata-rata tugas tambahan: "))
    
      if tugas_tambahan > 70:
        print("Lulus dengan predikat C")
      else:
        print("Tidak lulus")

else:
  print("Nilai tidak valid")