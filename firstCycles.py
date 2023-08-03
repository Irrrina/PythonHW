heads = 0
tails = 0
print("Введите количество монеток")
n = input()
n = int(n)
for i in range(n):
    side = int(input(f"Если {i+1} монетка лежит решкой напишите 0, орлом - 1: "))
    # заносим в счетчики решки и орлы
    if side == 1:
        heads += 1 
    elif side == 0:
        tails += 1
    # учитываем ошибку ввода
    else:
        print ("будьте внимательнее")
        break
# проверяем чего больше решек или орлов
if heads > tails:
    print (f"Нужно превернуть {tails} монеток")
else:
    print (f"Нужно превернуть {heads} монеток")

