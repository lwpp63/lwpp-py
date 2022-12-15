class Vehicle:
    def __init__(self,name,model,color,**kwargs):
        self.name=name
        self.model=model
        self.color=color
        if 'passenger' in kwargs:
            self.passenger=kwargs['passenger']
        else:
            self.passenger = 2
        if 'hp' in kwargs:
            self.hp=kwargs['hp']
        else:
            self.hp = 0
        # if 'fwd' in kwargs:
        #     self.fwd=kwargs['fwd']
        # else:
        #     self.fwd ='2x2'

    def __str__(self):
        return f"{self.name} {self.model}({self.hp}),{self.color}"

    def tunning(self,power):
        self.hp=self.hp+power

car=Vehicle('bmw','740i','black',passenger=5,hp=100)
print(f'car = {car}')
car.tunning(249)
print(f'car.tunning(249) = {car.hp}\n')
car_1=Vehicle('bmw','520i','blue',passenger=4)
print(f'car_1 = {car_1}')

class Auto(Vehicle):
    def __init__(self, name, model, color, **kwargs):
        super().__init__(name,model,color,**kwargs)
        if'fwd' in kwargs:
            self.fwd=kwargs['fwd']
        else:
            self.fwd='2x2'

    def __str__(self):
        return f"{self.name}({self.fwd}) {self.model}({self.hp}),{self.color}"

car_2=Auto('audi','A7','white',passenger=5,hp=200,fwd='4х4')
print(f'car_2 = {car_2}')

class Plane(Vehicle):
    def __init__(self, name, model, color, **kwargs):
        super().__init__(name,model,color,**kwargs)
        # if'passenger' in kwargs:
        #     self.passenger=kwargs['passenger']
        # else:
        #     self.passenger=50

        if 'max_height' in kwargs:
            self.max_height = kwargs['max_height']
        else:
            self.max_height = 5000
    def __str__(self):
        return f"{self.name}(pass:{self.passenger}) {self.model}(max_h:{self.max_height}),{self.color}"

plane=Plane('Airbas','A320','white',passenger=200,max_height=10000)
print(f'plane = {plane}')
