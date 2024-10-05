import random
angka_rahasia = random.randint(1, 100)
print("ketik '0' untuk keluar dari permainan.")
print(angka_rahasia)
for i in range(5): 
	try:
		tebakan = int(input(f"Percobaan ke-{i+1}, masukkan angka tebakanmu: "))
		if tebakan == 0:
			print("Kamu telah menyerah. Permainan selesai.")
			break
		if tebakan == angka_rahasia:
					print("Selamat! Tebakanmu benar!")
					break
		elif tebakan < angka_rahasia:
					print("Angka terlalu kecil.")
		else:
					print("Angka terlalu besar.")
	except ValueError:
		print("Input tidak valid masukkan angka")
print(f"Maaf, kamu kehabisan percobaan. Angka yang benar adalah {angka_rahasia}.")
		


    