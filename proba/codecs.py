import  codecs, os, datetime

try:
    with codecs.open('with_3.txt', 'a','utf-8') as ww:
        start = datetime.datetime.now()
        ww.write(f'1.{start.strftime("%X")}  запишем в with_3 файл!' + '\n')
        print(f'2.Ещё что-то запишем в \"{start.strftime("%c")}\"!', file=ww)
        ww.close()
except:
    print(f'Произошла какая-то ошибка! в {datetime.datetime.now().strftime("%X")}')


w=codecs.open('with_3.txt','r','utf-8').read()
print(w)

os.remove('with_3.txt')
print(f'3.Удалим файл with_3.txt! в {datetime.datetime.now().strftime("%X")}')