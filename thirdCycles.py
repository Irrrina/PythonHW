
print("Введите число N")
Number = input()
Number = int(Number)
k=0
stepen=1
for k in range(Number):
    stepen = 2**k
    if stepen < Number:
        print(stepen, end=" ")
    else:
        break