some_source = [1, 2, 3, 4]
empty_list = []

for stuff in some_source:
    empty_list.append(stuff)

filled_list = empty_list
del empty_list

print(filled_list)