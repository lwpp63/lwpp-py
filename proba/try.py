class MyException_2(Exception):
    massage="12).Sorry, no numbers below zero"
y = -1
try:
    if y < 0:
      raise MyException_2
except MyException_2:
    print(f'777.{MyException_2.massage}')


a,b,c = [33,77,4,9,22],[11,12,19,0,2],[0,1,2,3,4,5,6]
for i in range(7):
    try:
        d = a[i]*b[i]/c[i]
        print(f'{i}).Good')
    except ZeroDivisionError:
       print(f'{i}).ZeroDivisionError')
    except IndexError:
       print(f'{i}).IndexError')

try:
  print(x/0)
except NameError:
  print("8).Variable 'x' is not defined!")
except:
  print("9).Something else went wrong!")

class MyException(Exception):
    massage='10).Custom MyException'

try:
    raise MyException
except MyException:
    print(f'999.{MyException.massage}')

y = -1
if y < 0:
  raise Exception("11).Sorry, no numbers below zero")
