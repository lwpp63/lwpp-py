class Kettle:
    def turn_on(self):
        print('Нажали кнопку!')
        self.__boil()
        self.__check_temperature()
        self.__beep()
        self.__turn_off()

    def __boil(self):
        print('Разогревание воды!')

    def __check_temperature(self):
        print('Проверяем температуру воды?')

    def __beep(self):
        print('Подаём звуковой сигнал!')

    def __turn_off(self):
        print('Автоматическое выключение!')
print('class Kettle')
my_kettle= Kettle()
my_kettle.turn_on()
print('\n class Kettle_2')
class Kettle_2:
    def turn_on(self):
        print('Нажали кнопку!')
        self.__boil()
        self.__check_temperature()
        self.__beep()
        self._turn_off()

    def __boil(self):
        print('Разогревание воды!')

    def __check_temperature(self):
        print('Проверяем температуру воды?')

    def __beep(self):
        print('Подаём звуковой сигнал!')

    def _turn_off(self):
        print('Автоматическое выключение!')

my_kettle_2= Kettle_2()
my_kettle_2.turn_on()
my_kettle_2._turn_off()
print('my_kettle._Kettle__beep()')
my_kettle._Kettle__beep()