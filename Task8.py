import random
LIST_SIZE = 10
RANDOM_UPPER_BOUND = 10

listForWork_1 = []
listForWork_2 = []
listWithDifferance = []

for _ in range(0, LIST_SIZE):
    listForWork_1.append(random.randint(0, RANDOM_UPPER_BOUND))
    listForWork_2.append(random.randint(0, RANDOM_UPPER_BOUND))
print(listForWork_1)
print(listForWork_2)


for i in listForWork_1:
    if i not in listForWork_2:
        listWithDifferance.append(i)

print(listWithDifferance)
