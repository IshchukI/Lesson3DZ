word = input("Введитте слово: ")

for i in range(0, len(word)):
    print(word[len(word)-1-i], end="")

