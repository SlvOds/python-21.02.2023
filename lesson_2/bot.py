# я попытался подойти  креативно к выполнению задачи и построить диалоговое окно

print("Привіт, людино!")  # початок бесіди

name = ""
while not name.strip():  # не дозволяю залишити пустим ім я користувача
    name = input("Я бот Петро. А як твоє ім'я? ")

print(f"Приємно, {name}!. Радий знайомству")

while True:  # цикли я чесно не зрозумів і подивився відповідь в гугл
    age = input("Мені 2 дні. По вашим людським міркам я ще немовля, а який твій вік? ")
    if age.isnumeric():
        age = int(age)
        break  # особливо це
    else:
        print("Будь ласка реальний вік.")  # і весь цикл в цілому щось не до кінця зрозумів

if age <= 0:  # градація віку користувача
    print(f"{age} , а ти точно існуєш?")
elif age <= 6:
    print(f"{age} , а ти теж дитина")
elif age <= 18:
    print(f"{age} , вже майже дорослий")
elif age <= 25:
    print(f"{age}. Вітаю тебе зріла особа")
elif age <= 60:
    print(f"{age}. Я мабуть перейду на ви")
else:
    print(f"{age}. Вітаю мудрець")

print("Я чув, що зараз у вас в моді фільми по коміксах.")

favorite_movies = """ Людина павук,
 Залізна людина,
 Местники, 
 Капітан Америка,
 Бетмен,
 Супермен,
 Дедпул,"""

movies = " " + input("Які саме тобі подобаються? Дай пораду") + ","

if movies in favorite_movies:
    print("О велике дякую) я чув що це найпопулярніші супергерої")
else:
    print("Ніколи не чув, дякую за пораду")

# я не до конца понял момент с прерыванием выполнения программы пользователем (как это сделать в любом месте
# выполнения программы. Все мои попытки заканчивались тем, что код прерывался именно там где я и ставил в коде команду прервать)
# а делать его просто в конце не совсем интересно