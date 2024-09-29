import json

# Загрузка списка студентов
with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Печатаем заголовок
print(f"{'Предмет'} {'Дата экзамена'}")

# Заполняем данные
for student in data['students']:
    for grade in student['grades']:
        print(f"{grade['subject']} {grade['exam_date']}")
