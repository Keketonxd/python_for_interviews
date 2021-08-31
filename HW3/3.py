keys = [1, 2, 3, 4, 5, 6]
values = [1, 2, 3, 4]
dict = {}
# для избежания дубликатов ключей
keys = list(set(keys))

while len(keys) != len(values):
    if len(keys) > len(values):
        values.append(None)
    else:
        values.pop()

for i in range(len(keys)):
    dict[keys[i]] = values[i]
print(dict)
