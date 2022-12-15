import sys
from pprint import pprint

pprint(sys.path)
def calculator(expression):
    allowed = '+-/*'
    www=[sing in expression for sing in allowed]
    print(f'www = {www}')
    if not any(sing in expression for sing in allowed):
        raise ValueError(f'Выражение должно содержать хотя-бы один знак {allowed} действия')

    for sing in allowed:
        if sing in expression:
            try:
                left, right = expression.split(sing)
                left, right = int(left), int(right)
                if sing == '+':
                    return f'{left} + {right} = {left + right}'
                elif sing == '-':
                    return f'{left} - {right} = {left - right}'
                elif sing == '*':
                    return f'{left} * {right} = {left * right}'
                elif sing == '/':
                    return f'{left} : {right} = {left / right}'
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать два целых и один знак!')


if __name__ == '__main__':
    print(calculator('27+-9'))
