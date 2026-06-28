classrooms = int(input())

lst = []
for class_room in range(classrooms):
    students = int(input('Кол-во учеников: '))
    temp_lst = []
    for student in range(students):
        person = input('Ученик: ').split(' ')
        temp_lst.append(person[1])
    lst.append(temp_lst)
# lst = [[['q', '2'], ['w', '4']], [['g', '5'], ['f', '4']]]
print(lst)









