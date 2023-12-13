abc_dict = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4,
            'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8,
            'I' : 9,'J' : 10,'K' : 11,'L' : 12,
            'M' : 2,'N' : 3,'O' : 5,'P' : 10,}
unique_dict = {}
repeat_values = []
for key, value in abc_dict.items():
    if value not in unique_dict:
        unique_dict [value] = key
    else:
        # repeat_values.append(key)

print(unique_dict)
print(repeat_values)

