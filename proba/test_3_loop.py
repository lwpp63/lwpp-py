x = int(input('Введите число для расчёта факториала: '))
count = 1
y = 1
sum = ''
while count <= x:
    if count == 1:
        sum = str(count)
        count +=1
    else:
        sum = sum + '*' + str(count)
        y = y*count
        count +=1
        print(sum + ' = ', y)
else:
    print('Всё! Факториал ' + str(x) + ' равен ', y)
    
#Цикл while
a = ''
while len(a)<7:
    b = input('Введите текст: ')
    if b == '5':
        print('Введено: ',b,' . Повторим.')
        continue
    if b == '0':
        print('Введено: ',b,' . BREAK.')
        break
    a = a + b
else:
    print(a)

#Цикл for
s = 'My name is Pavel'
count = 1
for i in s:
    print(str(count) +'). ',i)
    count +=1
    if i == 's':
       break
print('В строке есть буква "s"')
        
    
