def func(x, y):
    z = (x+y)**2
    return z
print(f'(x+y)**2 = {func(3,2)}')

print(f'lambda x, y: (x+y)**2 (2,3) = {(lambda x, y: (x+y)**2)(2,3)}')

users = [
    'Jhon Dow 23',
    'Peter North 50',
    'Ben Affleck 47',
    'Anna Sedokova 35',
    'Vadim Kozachenko 60',
    'Valeriy Yagotin 61'
]
print('Сортировка по имени:')
users.sort()
print(f'users.sort() = {users}')
print('Сортировка по возрасту:')
users.sort(key = lambda w: w.split(' ')[-1])
print(f"users.sort(key = lambda w: w.split(' ')[-1]) = {users}")
print('Сортировка по:')
users.sort(key = lambda w: w.split(' '))
print(f"users.sort(key = lambda w: w.split(' ')) = {users}")

welcome = lambda user: print('Welcome, ' + user + '!')
welcome('Anon')