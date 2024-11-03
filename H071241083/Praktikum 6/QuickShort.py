def QuickShort(arr):
    if len(arr) <= 1:
        return arr
    else:
        Pivot = arr[len(arr) // 2]
        Kiri = [x for x in arr if x < Pivot]
        Tengah = [x for x in arr if x == Pivot]
        Kanan = [x for x in arr if x > Pivot]
        return QuickShort(Kiri) + Tengah + QuickShort(Kanan)
    
arr = ['1','8','2','5','4','7', '6']
short = QuickShort(arr)
print(short)