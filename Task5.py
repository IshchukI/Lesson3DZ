num_A = int(input("Введите число А: "))
num_B = int(input("Введите число В: "))

if num_A < num_B:
    print("По возрастанию: ", end="")
    while num_A != num_B + 1:
        print(num_A, end=" ")
        num_A += 1
else:
    print("Число А должно быть меньше В")