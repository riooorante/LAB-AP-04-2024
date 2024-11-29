import re

def validasi_string(s):
    if len(s) != 45:
        return False
    
    front = r'^[A-Za-z02468]{0,40}'

    end = r'[13579\s]{5}$'
    
    full = front + end

    if re.match(full, s):
        return True
    else:
        return False


s1 = "x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo139 7"  # Input valid
s2 = "2222222223aaaaaaaaaa2222222222aaaaaaaaaa13 57"    # Input tidak valid

print(validasi_string(s1))  
print(validasi_string(s2))  