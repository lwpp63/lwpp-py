class Animal:
    legs=4
    tail=1
    def voice(self,zvuk):
        print(f'{zvuk}!!')

# class Cat():
#      def voice(self):
#         print('Мяу - мяу!!!')
#
#
# class Dog():
#     def voice(self):
#         print('Гав - гав!!!')
#
#
# class Bull():
#     def voice(self):
#         print('Му - му!!!')

cat_1,cat_2,cat_3=Animal(),Animal(),Animal()
dog_1,dog_2,dog_3=Animal(),Animal(),Animal()
bull1,bull2,bull3=Animal(),Animal(),Animal()

farm_band=[cat_1,dog_1,bull1,cat_2,dog_2,bull2,cat_3,dog_3,bull3]
i=1
for animal in farm_band:
    print(i)
    if isinstance(animal,Animal):
        animal.voice('1). Мяу - мяу')
    if isinstance(animal,Animal):
        animal.voice('2). Гав - гав')
    if isinstance(animal,Animal):
        animal.voice('3). Му - му')
    i=i+1

