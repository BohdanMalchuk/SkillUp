# Пользователь вводит 3 числа. Нужно найти сумму и произведение чисел.
a=2
b=4
c=6
d=a+b+c
e=a*b*c
print("Cумма =", d)
print("Произведение =", e)
#
a=float(input( ))
b=float(input( ))
c=float(input( ))
d=a+b+c
e=a*b*c
print("Сумма =", d)
print("Произвидение =", e)


# # Пользователь вводит Имя и Фамилию. Нужно вывести приветствие для пользователя в новой системе.
name = input("Enter your first name: ") + " " + input("Enter your surname: ")
print("Hello, dear", name)

# # Пользователь вводит количество метров. Нужно конвертировать данные в километры и миллиметры.
metr=float(input("Метры"))
km=metr/1000
mm=metr*1000
print("Kilometr =", km)
print("Milimetr =", mm)