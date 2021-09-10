"""HW01: Testing triangle classification

   Author: Jose J. Cruz
   CWID: 10467076
"""

from typing import List


def is_equilateral(*arg: tuple[int]):
    if len(arg) != 3:
        raise Exception('Requires three sides')

    total: int = 0
    for side in arg:
        if not isinstance(side, int):
            raise TypeError('Side must be an int')
        if side <= 0:
            raise ValueError('The side can\'t be lower or equal to Zero ')
        total += side

    return (total / 3) == arg[0]


def is_isosceles(*arg: tuple[int]):
    if len(arg) != 3:
        raise Exception('Requires three sides')

    for side in arg:
        if not isinstance(side, int):
            raise TypeError('Side must be an int')
        if side <= 0:
            raise ValueError('The side can\'t be lower or equal to Zero ')

    return arg[0] == arg[1] or arg[1] == arg[2] or arg[2] == arg[0]


def is_right(*arg: tuple[int]):
    if len(arg) != 3:
        raise Exception('Requires three sides')

    for side in arg:
        if not isinstance(side, int):
            raise TypeError('Side must be an int')
        if side <= 0:
            raise ValueError('The side can\'t be lower or equal to Zero ')

    sides = sorted(arg)

    return (pow(sides[0], 2) + pow(sides[1], 2)) == pow(sides[2], 2)


def classify_triangle(*arg: tuple[int]) -> str:
    if is_equilateral(arg[0], arg[1], arg[2]):
        return 'equilateral'
    elif is_isosceles(arg[0], arg[1], arg[2]):
        return 'isosceles'
    elif is_right(arg[0], arg[1], arg[2]):
        return 'right'
    else:
        return 'scalene'


def main():
    """Main program function"""
    sides: List[int] = []
    while not len(sides) == 3:
        user_input = input(f'Insert the length of the side {len(sides) + 1}: \n')
        try:
            side = int(user_input)
        except ValueError:
            print(f'The value {user_input} is not an integer, please try again')
        except:
            print("Something else went wrong, Please try again")
        else:
            if side <= 0:
                print('The side can\'t be lower or equal to Zero ')
                continue
            sides.append(side)

    triangle_type: str = classify_triangle(sides[0], sides[1], sides[2])

    print(f'\n-----------------------\n\nIs a "{triangle_type}" triangle')


if __name__ == "__main__":
    main()
