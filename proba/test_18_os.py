import os, codecs

list_paths = []

for adress, papka, file in os.walk('C:\\Users\lwpp6\Desktop\Python'):
    list_paths.append(adress)
    i = 1
    for f in file:
        full_path = os.path.join(adress, f)
        list_paths.append(str(i).rjust(5)+')'+full_path)
        i+=1

r = codecs.open('test_19_os.txt', 'w','utf-8')
r.write('Строка нашего текста в test_19_os.txt \n')
for k in list_paths:
    r.write(k + '\n')
r.close()

w = codecs.open('test_19_os.txt','r','utf-8')
print(w.read())
w.close()

    
ww = codecs.open('test_19_os.txt','r','utf-8')
print('type(ww) = ',type(ww))
print('ww.readline 1 = ',ww.readline())
print('ww.readline 2 = ',ww.readline())
print('ww.readline 3 = ',ww.readline())
print('str(ww).rjust(75) =',str(ww).rjust(75),'\n')

i = 100
for str in ww:
    if i<110:
       if 'Новая папка' in str:
           print(i,str.replace("\n",""))
           i+=1
    else:
        print('Все строки напечатаны!')
        break
ww.close()
