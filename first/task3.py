'Знайти суму усіх цілих чисел у інстервалі обмеженному дійсними чіслами'
num1 = float(input('num1: '))
num2 = float(input('num2: '))
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
if num1 > int(num1):
    num1 = int(num1)+1
else:
    num1 = int(num1)
num2 = int(num2)
suma = 0
for i in range(num1, num2+1):
    suma += i
print(suma)
