import random
LIST_SIZE = 10
RANDOM_UPPER_BOUND = 10

listForWork = []
copyOfListForWork = []

for _ in range(0, LIST_SIZE):
    listForWork.append(random.randint(0, RANDOM_UPPER_BOUND))

for item in listForWork:
    copyOfListForWork.append(item)

print(f"l1: {listForWork}")
print(f"l2: {copyOfListForWork}")
