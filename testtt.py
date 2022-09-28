list1 = ['best', 'car', 'pizza', 'want']
list2 = ['want']
Array = []

for l1 in list1:
    for l2 in list2:
        if l1 == l2:
            Array.append(l1)
print(Array)