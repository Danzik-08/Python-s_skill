import re
import operator
from functools import reduce


def solution1(arg):
    return list(map(lambda x: int(re.sub(r'\D', "", x)[-1::-1]), arg))


def solution2(arg):
    return list(map(lambda a: a[0]*a[1], arg))


def solution3(arg):
    return list(filter(lambda x: x % 6 in [0, 2, 5], arg))


def solution4(arg):
    return list(filter(lambda a: bool(a) and True, arg))


def solution5(arg):
    return list(map(lambda x: operator.setitem(x, "square", x["length"]*x["width"]), arg))


def solution6(arg):
    return list(map(lambda room: dict(**room, square=room['width']*room['length']), arg))


def solution7(arg):
    return reduce(set.intersection, arg)


def solution8(arg):
    return reduce(lambda a, b: operator.setitem(a, b, a.get(b, 0) + 1) or a, arg, {})


def solution9(arg):
    return list(map(operator.itemgetter('name'), filter(lambda x: x["gpa"] > 4.5, arg)))


def solution10(arg):
    return list(filter(lambda x: sum(map(int, x[1::2])) == sum(map(int, x[::2])), arg))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
