import sys
from pprint import pprint

#pprint(sys.path)
i=0
def calculator(expression):
    allowed = '+-/*'
    www=[sing in expression for sing in allowed]
    print(f'{i}).www = {www}')

    if not any(sing in expression for sing in allowed):
        raise ValueError(f'Выражение должно содержать хотя-бы один знак {allowed} действия')

    for sing in allowed:
        if sing in expression:
            try:
                left, right = expression.split(sing)
                left, right = int(left), int(right)
                if sing == '+':
                    return left + right
                elif sing == '-':
                    return left - right
                elif sing == '*':
                    return left * right
                elif sing == '/':
                    return left / right
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать два целых и один знак!')


if __name__ == '__main__':
    print(f"1).calculator('27+-9') = {calculator('27+-9')}")