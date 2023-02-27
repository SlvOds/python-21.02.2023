# :1 Написати програму що рахує витрати на паливо.
# :2 Вхідні дані:
# :3 витрачання палива автомобілем за 100км
# :4 сьогоднішня ціна 1 л палива
# :5 скільки кілометрів треба здолати
# :6 На виході:
# :7 скільки грошей на це піде, округлено до двох цифр після коми

import math

gas_expenses = input("Enter amount of fuel per 100 km")  # amount of fuel per 100 km
a = float(gas_expenses)

gas_price = input("Enter price of fuel for 1 litter")
b = float(gas_price) # change "str" to "float"

distance = input("Kilometers to go") # distance to go
d = float(distance) # change "str" to "float"

gas_expenses_for_distance = (d / a) # amount of fuel need for full distance
c = float(gas_expenses_for_distance) # change "str" to "float"

money_expenses = (b * c) # amount of money need for the trip
e = float(money_expenses)  # change "str" to "float"
rounded_e = (round(e, 2))

print(f"Амount of money {rounded_e} UAH")

# код кривой ибо в этом я вообще нюб

#Написати програму, що рахує абонплату за комунальним лічильника (наприклад, електроенергії або газу).
#Вхідні дані:
#попередні показання
#теперішні показання
#тариф.
#На виході:
#скільки потрібно сплатити, округлено до двох цифр після коми


a = float(input("Введіть показання лічільника за попередній місяць"))
b = float(input("Введіть показання лічільника станом на сьогодні"))
c = float(b - a) # використане за місяць
print(f"Використано за місяць {c} кіловатт")

d = float(1.68)  # постійний тариф постачальника за кіловатт електроенергії

e = float(d * c) #формула суми для сплати
rounded_e = (round(e, 2))
print(f"Ваша сумма до сплати {rounded_e} грн")