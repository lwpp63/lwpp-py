users = {
    (15,35),
    (15,45),
    (25,25),
    (20,30),
    (30,25),
    (15,50)
}
users_2 = [
    (15,35),
    (15,45),
    (25,25),
    (20,30),
    (30,25),
    (15,50)
]
print(f'users = {users}')
print(f'-1).sorted(users) = {sorted(users)}')
print(f'users_2 = {users_2}')
print(f'0).sorted(users_2) = {sorted(users_2)}')
def squares(users):
    sqs=[]
    for w_l in users:
        sqs.append(w_l[0]*w_l[1])
    return sqs
print(f'1).Площади участков пользователей равны: {squares(users)}')

p=[w_l[0]*w_l[1] for w_l in users]
print(f'2).Площади участков пользователей равны: {p}')
p_2=(w_l[0]*w_l[1] for w_l in users)
print(f'22).Площади участков пользователей равны: {list(p_2)}')
s=map(lambda w_l:w_l[0]*w_l[1],users)
print(f'3).Площади участков пользователей равны: {s}')
sqs=list(s)
print(f'4).Площади участков пользователей равны: {sqs}')

def myfunc(a, b):
  return a + b
a=('apple', 'banana', 'cherry')
b=('orange', 'lemon', 'pineapple')
print(f'a + b = {myfunc(a, b)}')
x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(f"5).map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')) = {x}")
xx=list(x)
print(f"6).list(map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))) = {xx}")
xxx = map(lambda a,b:a+b, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(f"7).map(lambda a,b:a+b, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')) = {list(xxx)}")
print('Регистронезависимое сравнение строк!!!')
sort = sorted("This is a test string from Andrew".split(), key=str.lower)
print(f'8).orted("This is a test string from Andrew".split(), key=str.lower) = {sort}')

students=[('Amanda','161cm','51kg'), ('Patricia','165cm','61kg'), ('Marcos','191cm', '101kg')]
print(f"9).students = {[('Amanda','161cm','51kg'), ('Patricia','165cm','61kg'), ('Marcos','191cm', '101kg')]}")
students_height = list(map(lambda x:x[1], students))
print(f'10).students_height = list(map(lambda x:x[1], students)) = {students_height}')

students_weight = list(map(lambda x:int(x[2][:-2]), students))
print(f'11).students_weight = list(map(lambda x:int(x[2][:-2]), students)) = {students_weight}')

elements = [1,2,3,4]
print(f'12).elements = {elements}')
elements_by2 = map(lambda x:x*2,elements)
print(f'13).elements_by2 = map(lambda x:x*2,elements) = {elements_by2}')
print(f'14).type(elements_by2) = {type(elements_by2)}')

elements_list = list(map(lambda x:x*2,elements))
print(f'15).elements_list = list(map(lambda x:x*2,elements) = {list(map(lambda x:x*2,elements))}')
print(f'16).type(elements_list) = {type(elements_list)}')


elements_set = set(map(lambda x:x*2,elements))
print(f'17).elements_set = set(map(lambda x:x*2,elements)) = {elements_set}')
print(f'18).type(elements_set) = {type(elements_set)}')


elements_tuple = tuple(map(lambda x:x*2,elements))
print(f'19).elements_tuple = tuple(map(lambda x:x*2,elements)) = {elements_tuple}')
print(f'20).type(elements_tuple) = {type(elements_tuple)}')

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(f'21).cars.sort(key=myFunc) = {cars}')



