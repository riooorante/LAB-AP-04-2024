match Jumlah_data:
#     case jumlah_data if Jumlah_data < 10 :
#         if waktu_penggunaan == "y" and pengguna == "y":
#             print("Paket yang sesuai: paket A")
#         else:
#             print("Tidak ada paket yang cocok")
#     case jumlah_data if 10<jumlah_data<50:
#         if waktu_penggunaan == "n" and pengguna == "y":
#             print("Paket yang sesuai: paket B ")
#         else:
#             print("Tidak ada paket yang cocok")
#     case jumlah_data if jumlah_data>50:
#         if waktu_penggunaan == "n" and pengguna == "y" or pengguna == "n":
#             print("Paket yang sesuai: paket C")
#         elif waktu_penggunaan == "y" and pengguna == "n":
#             print("paket yang sesuai: paket D")
#         else:
#             print("Tidak ada paket yang cocok")