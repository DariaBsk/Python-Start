import random

students_basa = {}
students_name = []
subjecs_list = []

students_last_name = ['Абаев', 'Авдеев', 'Агапов', 'Агафонов', 'Агафонова', 'Агеев', 
'Агеева', 'Акимов', 'Асеев', 'Бабушкин', 'Бабушкина', 'Баженов', 'Баженова', 'Балашов', 'Балашова', 
'Баранов', 'Баранова', 'Барсуков', 'Барсукова', 'Вавилов', 'Вавилова', 'Вагин', 'Вагина', 'Васильев', 
'Васильева', 'Вдовин', 'Вдовина', 'Верещагин', 'Верещагина', 'Гаврилов', 'Гаврилова', 'Гайдуков', 'Гайдукова', 
'Гакабов', 'Гакабова', 'Галкин', 'Галкина', 'Герасимов', 'Герасимова', 'Давыдов', 'Давыдова', 'Дадаева', 'Дадина', 
'Данилов', 'Данилова', 'Дарвина', 'Дашков', 'Дашкова', 'Дегтярев', 'Евдокимов', 'Евдокимова', 'Евсеев', 'Евсеева', 
'Егоров', 'Егорова', 'Ежов', 'Ежова', 'Елизаров', 'Елизарова', 'Жаров', 'Жарова', 'Жданов', 'Жданова', 'Жилин', 'Жилина', 
'Жириновская', 'Жириновский', 'Жуков', 'Жукова', 'Завьялов', 'Завьялова', 'Заец', 'Зайцев', 'Зайцева', 'Захаров', 'Захарова', 
'Зверев', 'Зверева', 'Звягинцев', 'Иванов', 'Иванова', 'Ивашов', 'Ивашова', 'Игнатов', 'Игнатова', 'Игнатьев', 'Игнатьева', 
'Измайлов', 'Измайлова', 'Казаков', 'Казакова', 'Казанцев', 'Казанцева', 'Калачев', 'Лихачев', 'Лосев', 
'Луговой', 'Матросов', 'Носков', 'Орлов', 'Панин', 'Рублев', 'Степанов', 'Толоконников']
subjecs_list_rand = ['Русский язык', 'Литература', 'История', 'Георграфия', 'Физика', 'Информатика', 'Алгебра', 'Геометрия', 'Химия']
grade_list = [1, 2, 3, 4, 5]


#0 - Добавление нового студента (Поля - имя, фамилия)
def create_student(student):
    if student not in students_name:
        students_name.append(student)
        students_basa[student] = {}
        for subject in subjecs_list:
            students_basa[student][subject] = []
        print(f'Добален новый студент: {student}')
        print_students_basa()
    else:
        print("Такой студент уже есть в программе!")

#1 - Добавление предмета
def add_subject(subject):
    if subject not in subjecs_list:
        subjecs_list.append(subject)
        for student in students_name:
            students_basa[student][subject] = []
            print(f"Добавлен новый предмет: {subject}")
            print_students_basa()
    else: 
        print("Такой предмет уже есть в программе!")

def add_grade(student, subject, grade):
    students_basa[student][subject].append(grade)
    print(f'Добалена оценка {grade} студенту {student} по предмету {subject}')
    print_students_basa()

def show_students_names():
    for student in students_name:
        print(student)

def show_student_journal(student_name):
    print(students_basa[student_name])

def random_list():
    for i in range (0, len(students_last_name)):
        random_index = random.randint(0, len(students_last_name) - 1)
        student = (students_last_name[random_index])
        if student not in students_name:
            students_name.append(student)
            students_basa[student] = {}
    for i in range (len(subjecs_list_rand)):
        random_index = random.randint(0, len(subjecs_list_rand)-1)
        subject = (subjecs_list_rand[random_index])
        if subject not in subjecs_list:
            subjecs_list.append(subject)
        for student in students_name:
            for subject in subjecs_list:
                students_basa[student][subject] = []
                for i in range(1, 7):
                    grade = random.randint(1, 5)
                    students_basa[student][subject].append(grade)
    for student, subject in students_basa.items():
        print(student, subject)

def print_students_basa():
    for student, subject in students_basa.items():
        print(student, subject)

def write_file():
    with open('Students_basa.txt', 'a') as file:
        for student, subject in students_basa.items():
            student_list = f'{student}, {subject}'
            file.write(student_list)
            file.write('\n')
    file.close()


def reading_file():
    with open('Students_basa.txt', 'r') as file:
       while True:
           student_list = file.readline()
           students_basa = student_list.strip()
           print_students_basa()
           if not student_list:
            break
    file.close()