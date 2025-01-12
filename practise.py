lists = [123, 23, 3]
for r in lists:
    if r == 23:
        lists.remove(lists[-1])
print(lists)
