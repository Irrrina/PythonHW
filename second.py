# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.

# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.

n = 48

# Введите ваше решение ниже

if n % 6 == 0:
    # Раскладываем число на три числа в пропорции 1:4:1
    num1 = n // 6
    num2 = 4 * num1
    num3 = num1
   
   
    print(f"{num1} {num2} {num3}")