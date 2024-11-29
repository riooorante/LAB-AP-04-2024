def quicksort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[1]
        less = [x for x in data if x < pivot]
        equal = [x for x in data if x == pivot]
        more = [x for x in data if x > pivot]
        return quicksort(less) + equal + quicksort(more)

data = [33, 10, 59, 27, 78, 2, 4, 4]
sorted_data = quicksort(data)
print("Data sebelum diurutkan:", data)
print("Data setelah diurutkan:", sorted_data)