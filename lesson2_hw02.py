a = int (input ("Введите число  "))
b = int (input ("Укажите степень числа  "))
c = a ** b
print ("Результат 1: " ,c,".", "Тип:", type (c))
import math
d = math.pow(a,b)
print ("Результат 2: ",d,".", "Тип:", type (d))
print ("Значение c больше значения d?")
print (c>d)
