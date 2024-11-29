def sub_string(string):
    urutan = [ ]
    for i in range(1, len(string) + 1):             
        for j in range(len(string) - i + 1):
            urutan.append(string[j:j+i])
    
    for karakter in urutan:
        print(karakter)

#meminta input
string = input("Masukkan string: ")
sub_string(string)