nilai_akhir = int(input("Masukkan Nilai Akhir: "))

if 0<=nilai_akhir<=100:
  kehadiran = int(input("Masukkan Persentase Kehadiran: "))
  if kehadiran < 75:
    print("Tidak Lulus")
  elif nilai_akhir >= 85:
    print("Lulus dengan Predikat A")
  elif nilai_akhir >= 70:
    print("Lulus dengan Predikat B")
  elif nilai_akhir >= 60:
    print("Lulus dengan Predikat C")
  else:
    tugas_tambahan = int(input("Masukkan nilai rata-rata tugas tambahan: "))

    if tugas_tambahan > 70:
      print("Lulus dengan Predikat C")
    else:
      print("Tidak Lulus")
else:
  print("Nilai Tidak Valid")