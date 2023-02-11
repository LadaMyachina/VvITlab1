groupmates = [
    {
        "name": "Мария",
        "surname": "Дедова",
        "exams": ["Философия", "АиГ", "ВвИТ"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Андрей",
        "surname": "Чекулаев",
        "exams": ["Философия", "АиГ", "ВвИТ"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Максим",
        "surname": "Тарасов",
        "exams": ["Философия", "АиГ", "ВвИТ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Яна",
        "surname": "Козлова",
        "exams": ["Философия", "АиГ", "ВвИТ"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Вероника",
        "surname": "Землякова",
        "exams": ["Философия", "АиГ", "ВвИТ"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Максим",
        "surname": "Морозов",
        "exams": ["Философия", "АиГ", "ВвИТ"],
        "marks": [5, 4, 5]
    }
]

def print_students(students):   #функция вывода всех студентов
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20)) #указали кодировку (u) и по красоте вывод списка
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)






def sum_stud(students, a):
    for student in students:
        student['average'] = (sum(student['marks']))/len(student['marks'])
        if student['average'] > a:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


a = float(input("Введите средний балл: "))
sum_stud(groupmates, a)




