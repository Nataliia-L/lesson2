a = int (input ("Введите число  "))
b = int (input ("Укажите степень числа  "))
val_1 = a ** b
print ("Результат 1: " ,val_1,".", "Тип:", type (val_1))
import math
val_2 = math.pow(a,b)
print ("Результат 2: ",val_2,".", "Тип:", type (val_2))
print ("Значение val_1 равно значению val_2?")
print (val_1==val_2)
