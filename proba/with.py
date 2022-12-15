import  codecs,os, datetime
open_file = codecs.open('with_1.txt', 'a','utf-8')
try:
    open_file.write('Что-то запишем в with_1 файл!' + '\n')
    print(100/0) #Ошибка деления на 0
    open_file.write('Ещё что-то запишем в этот файл!' + '\n')
except ZeroDivisionError:
    with codecs.open('with_2.txt', 'a','utf-8') as op_fl:
        op_fl.write('Что-то запишем в этот файл!' + '\n')
        print(100/0)#Ошибка деления на 0
        op_fl.write('Ещё что-то запишем в with_2.txt файл!' + '\n')
finally:
    open_file.close()
    print('1).Записали только первую строку в оба файла:with_1.txt и with_2.txt!!!')
    print('2).Но во втором случае, with_2.txt,  не надо закрывать файл, запись сохранится!')

    try:
        with codecs.open('with_3.txt', 'a','utf-8') as ww:
            ww.write('1.Что-то запишем в with_3 файл!' + '\n')
            print(f'2.Ещё что-то запишем в with_3 файл! {datetime.datetime.now().strftime("%X")}', file=ww)
            ww.close()
            print(f'3).Выведем на печать из файла with.py! в {datetime.datetime.now().strftime("%X")}')
    except:
        print('Произошла какая-то ошибка!')
