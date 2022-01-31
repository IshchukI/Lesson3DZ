import random
LIST_SIZE = 10
RANDOM_UPPER_BOUND = 10

listForWork = []
ListWithoutDuplicate = []

for _ in range(0, LIST_SIZE):
    listForWork.append(random.randint(0, RANDOM_UPPER_BOUND))
print(listForWork)

for i in listForWork:
    if i not in ListWithoutDuplicate:
        ListWithoutDuplicate.append(i)

print(ListWithoutDuplicate)
