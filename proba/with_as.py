from contextlib import contextmanager

class Resource:
    def __int__(self):
        self.opened = False

    def open(self, *args):
        print(f'Resource был открыт с аргументами = {args}')
        self.opened = True
    def __del__(self):
        print("Выполняется  __del__ всегда в самом конце!!!")
        if self.opened:
            print('Resource не закрыт, произошла утечка данных!!!')
    def action(self):
        print('Проводим определённые действия!')
    def my_func(self, x):
        print(f'my_func = {x}')
    def close(self):
        print(f'Resource был закрыт!!!')
        self.opened = False

if __name__ == '__main__':
    print('1). Обработка через try - exsept')
    resource = None
    try:
        resource = Resource()
        resource.open([22, 33, 44, 55])
        resource.action()
        resource.my_func("Hello")
       # raise ValueError('Hello')
    except:
        raise  #Повторить исключение
    finally:
        if resource:
            resource.close()

@contextmanager
def open_resource(*args):
    resource = None
    try:
        resource = Resource()
        resource.open(args,args[3])
        yield resource
    except Exception:
        raise  # Повторить исключение
    finally:
        if resource:
            resource.close()

print('2). Обработка через with - as')
with open_resource(11,12,13,14,15) as res:
        res.action()
        res.my_func('Привет!')
        #raise ValueError('STOP!')