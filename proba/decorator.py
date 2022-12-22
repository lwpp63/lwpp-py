import  datetime, time
print(f"Функция это полноправный объект! {__name__}")
print("Внутренняя функция может захватывать переменные из внешней!")
def summ(a, b, c):
    return (a + b)*c

def example(examp):
    print((f'1).Имя функции: {examp.__name__}, результат = {examp(1,2,3)}'))

def bot(x):
    def inner(y):
        print(f'2).x+y = {x+y}')
    inner(6)

def logger(fun):
    nachalo = time.time()
    start = datetime.datetime.now()
    def wrapper(a,b,c):
        print(f'3).fun.__name__ = {a+c} {fun.__name__} started in {start.strftime("%X")}')
        result = fun(a,b,c)
        print(f'4).fun.__name__ = {b+c} {fun.__name__} finished in {start.strftime("%X")}')
        print(f'start = {start.strftime("%f")} мс')

        return result
    konec = time.time()
    print(f"konec-nachalo = {nachalo-konec}")
    return wrapper

def logger_2(fun):
    start = datetime.datetime.now()
    def wrapper(*args):
        print(f'7).fun.__name__ =  {fun.__name__} started_2 in {start.strftime("%f")} мс')
        result = fun(*args)
        print(f'8).fun.__name__ =  {fun.__name__} finished_2 in {start.strftime("%f")} мс')
        return result
    return wrapper

@logger_2  #Декоратор
def sum_2(x,y,z,v):
    return (x*y/z)*v

if __name__=='__main__':
    func = summ
    print(f'summ = {sum}')
    print(f'func = {func}')
    example(summ)
    bot(10)
    function = logger(summ)
    print(f'5).function = {function}')
    print(f'6).function(2,3,4) = {function(2,3,4)}')
    print("Запись function = logger(summ) + function(2,3,4) соответствует записи: logger(summ)(2,3,4)")
    print(f'8).logger(summ)(2,3,4) = {logger(summ)(2,3,4)}')
    print(f'9).logger_2(sum_2)(5,6,7,8) = {logger_2(sum_2)(5,6,7,8)}')
    print(f"Можно ещё упростить: summ = logger(summ)")
    summ = logger(summ)
    print(f"10).summ = summ(9,8,7) = {summ(9,8,7)}")
    print("\n Работает декоратор '@logger_2'!")
    print(f'11).sum_2(3,4,5,6) = {sum_2(3,4,5,6)}')
