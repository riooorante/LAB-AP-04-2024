x=int(input("Masukkan nilai sisi pertama : "))
y=int(input("Masukkan nilai sisi pertama : "))
z=int(input("Masukkan nilai sisi pertama : "))

if x+y > z and x+z > y and y+z > x:
  
  if x==y==z:
    segitiga = 'Segitiga sama sisi'
  elif x==y or x==z or y==z:
    segitiga = 'Segitiga sama kaki'
  else:
    segitiga = 'Segitiga sembarang'
else:
  segitiga = 'Segitiga tidak valid'

print(segitiga)

