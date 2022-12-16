from math import pi

def circle_area(radius):
    if type(radius) not in [int,float]:
        print(f'type({radius}) = {type(radius)}')
        raise TypeError("Радиус должен быть числом >= 0!")
    if radius < 0:
        print(f'type({radius}) = {type(radius)}')
        raise ValueError("Radius can`t <= 0")

    return pi*pow(radius,2)

if __name__=='__main__':
    r_list = [2,9,7+9j,0,2+3j,True,[7],'nine',99]

    i=1
    for r in r_list:
        s = circle_area(r)
        print(f'{i}). Площадь окружности радиусом:{r} равна:{s}' )
        i+=1


