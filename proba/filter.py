users = {
    (15,35),
    (15,45),
    (25,25),
    (20,30),
    (30,25),
    (15,50)
}
def squares(us):
    sqs=us[0]*us[1]
    if sqs<=600:
        return True
    else:
        return False

f=filter(squares,users)
print(f'1).{f}')
print(f'2).{list(f)}')

p=[w_l[0]*w_l[1] for w_l in users]
med_p=round(sum(p)/len(p),2)
print(f'3).Площади участков пользователей равны: {p}')
print(f'4).Средняя площадь участков пользователей равна: {med_p}')

s=filter(lambda v_l:(v_l[0]*v_l[1]) < sum(p)/len(p), users)
print(f'5).Площади участков пользователей меньше средней:{list(s)}')


"""
    Программа для поиска совпадений между
    двумя списками, используя функцию filter()
"""

# Список строк с похожими элементами
list1 = ["Python", "CSharp", "Java", "Go"]
list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]

# функция, которая проверяет строки на вхождение
def filter_duplicate(string_to_check):
    if string_to_check in ll:
        return False
    else:
        return True

# Применение filter() для удаления повторяющихся строк
ll = list2
out_filter = list(filter(filter_duplicate, list1))
ll = list1
out_filter += list(filter(filter_duplicate, list2))

print("Отфильтрованный список:", out_filter)


"""
    Программа для удаления стоп-слов
    из строки используя функцию filter()
"""

# Список стоп-слов
list_of_stop_words = ["в", "и", "по", "за"]

# Строка со стоп-словами
string_to_process = "Сервис по поиску работы и сотрудников HeadHunter опубликовал подборку высокооплачиваемых вакансий в России за август."

# lambda-функция, фильтрующая стоп-слова
split_str = string_to_process.split()
#print(split_str)
filtered_str = ' '.join((filter(lambda s: s not in list_of_stop_words, split_str)))
print("Отфильтрованная строка:a", filtered_str)


"""
    Программа для поиска общих элементов в двух списках
    с использованием функции lambda и filter()
"""

# Два массива, имеющие общие элементы
arr1 = ['p','y','t','h','o','n',' ','3','.','0']
arr2 = ['p','y','d','e','v',' ','2','.','0']
out = list(filter(lambda it: it in arr1, arr2))
print("Отфильтрованный список:", out)


from operator import itemgetter
l1 = [(1, 2, 3), (3, 1, 1), (8, 5, 3), (3, 4, 2)]
# Сортировка по третьему элементу в кортеже
print(f'6).sorted(l1, key=itemgetter(2)) = {sorted(l1, key=itemgetter(2))}')
# Вывод: [(3, 1, 1), (1, 2, 3), (3, 4, 2), (8, 5, 3)]


from operator import itemgetter
# Создание списка словарей
d1 = [{'name': 'Paul', 'age': 30},
      {'name': 'Alex', 'age': 7},
      {'name': 'Eva', 'age': 3}]

# Сортировка по key(age) в словаре
print(f"7).sorted(d1, key=itemgetter('age')) = {sorted(d1, key=itemgetter('age'))}")
# Вывод: [{'name': 'Eva', 'age': 3}, {'name': 'Alex', 'age': 7}, {'name': 'Paul', 'age': 30}]