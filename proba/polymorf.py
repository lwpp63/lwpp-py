class Animal:
    legs=4
    tail=1
    def voice(self):
        print('Какой-то звук!!!')

class Cat(Animal):
     def voice(self):
        print(f'1). Мяу - мяу!!! {self.legs} лапы')


class Dog(Animal):
    def voice(self):
        print('2). Гав - гав!!!')


class Bull(Animal):
    def voice(self):
        print('3). Му - му!!!')

cat_1,cat_2,cat_3=Cat(),Cat(),Cat()
dog_1,dog_2,dog_3=Dog(),Dog(),Dog()
buii1,bull2,bull3=Bull(),Bull(),Bull()

farm_band=[cat_1,dog_1,bull2,cat_2,dog_2,bull2,cat_3,dog_3,bull3]

for animal in farm_band:
    if isinstance(animal,Cat):
        animal.voice()
    if isinstance(animal,Dog):
        animal.voice()
    if isinstance(animal,Bull):
        animal.voice()