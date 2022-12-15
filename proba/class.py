class Car:
    def __init__(self,name,model,color,**kwargs):
        self.name=name
        self.model=model
        self.color=color
        if 'hp' in kwargs:
            self.hp=kwargs['hp']
        else:
            self.hp = 120

    def __str__(self):
        return f"{self.name} {self.model},{self.color}"

    def tunning(self,power):
        self.hp=self.hp+power

audi=Car('Audi','A4 2.0','blue',hp=75)
bmw=Car('BMW','540i','black')
print(f'audi = {audi} bmw = {bmw}')

audi_hp=audi.hp
print(f'1).audi_hp = {audi_hp}')

bmw_hp=bmw.hp
print(f'2).bmw_hp = {bmw_hp}')

audi.audi='audi-7'
audi_audi=audi.audi
print(f'22).audi_audi = {audi_audi}')

bmw.bmw='bmw-7'
bmw_bmw=bmw.bmw
print(f'33).bmw_bmw = {bmw_bmw}')

audi.hp=200
audi_hp=audi.hp
print(f'3).audi.hp = {audi_hp}')

bmw.hp=300
bmw_hp=bmw.hp
print(f'4).bmw_hp = {bmw_hp}')

audi.tunning(150)
print(f'5).audi.hp = {audi.hp}')

bmw.tunning(-50)
print(f'6).bmw.hp = {bmw.hp}')

