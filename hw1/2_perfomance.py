"""
Сотрудникам учебного офиса нужно посчитать оценки студентов по каждому предмету.

Вводятся неизвестное число строк. Каждая строка содержит фамилию студента, предмет и оценку за этот предмет через пробел. Затем вводится одна строка "END".

После этого вводится фамилия студента.

Выведите оценки это студента по каждому предмету. Каждый предмет выводится с новой строки, затем через пробел выводится оценка по этому предмету. Названия предметов должны быть отсортированы в алфавитном порядке. Если у студента встречается больше одной оценки по одному предмету, учитывается последняя.

Формат ввода
Вводится неизвестное число строк, затем строка "END", означающая конец ввода. Затем вводится еще одна строка, означающую фамилию студента.

Формат вывода
Выведите ответ на задачу (строки формата "Предмет оценка").
"""
students_dict = {}

while True:
    line = input()
    if line.strip() == 'END':
        break
    last_name, subject, grade = line.split()

    if last_name not in students_dict:
        students_dict[last_name] = {}

    students_dict[last_name][subject] = grade

target_last_name = input()
subjects = sorted(students_dict[target_last_name].keys())

for subject in subjects:
    print(f'{subject} {students_dict[target_last_name][subject]}')
