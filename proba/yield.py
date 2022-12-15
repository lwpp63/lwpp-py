print('Код на Python3 для демонстрации использования ключевого слова "yield"')

# генерация нового списка, состоящего
# только из четных чисел
def get_even(list_of_nums):
    for i in list_of_nums:
        if i % 2 == 0:
           yield i


# инициализация списка
list_of_nums = [1, 2, 3, 8, 15, 42]
print(f'list(get_even(list_of_nums)) = {list(get_even(list_of_nums))}')
# вывод начального списка
print("1). До фильтрации в генераторе: " + str(list_of_nums))
print(f"2). До фильтрации в генераторе: {list_of_nums}")
# вывод только четных значений из списка
print("3). Только четные числа: ", end=" ")
for i in get_even(list_of_nums):
    print(i, end=" ")


# Данная Python программа выводит
# числа от 1 до 15, возведенные в куб,
# используя yield и, следовательно, генератор

# Функция ниже будет бесконечно генерировать
# последовательность чисел в третьей степени,
# начиная с 1
def nextCube():
    acc = 1

    # Бесконечный цикл
    while True:
        yield acc ** 3
        acc += 1  # После повторного обращения
        # исполнение продолжится отсюда


# Ниже мы запрашиваем у генератора
# и выводим ровно 15 чисел

count = 1
str_num = '\n 4). nextCube() = '
for num in nextCube():
    if count > 15:
        break
    str_num = str_num + str(num) +', '
    count += 1
print(str_num)

mylist = [x*x for x in range(5)]
def create_generator():
    for k in mylist :
      yield k*3
print(f"5). create_generator() = {list(create_generator())} ")