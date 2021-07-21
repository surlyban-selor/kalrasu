# def decorator(func):
#     def decorated(a, b):
#         print('삼각형 : ')
#         func(a, b)
#
#     return decorated
#
# @decorator
# def triangle(a, b):
#     while True:
#         if a < 0 or b < 0:
#             print('Error')
#         else:
#             break
#     c = (a * b) / 2
#     return c
#
#
# triangle(3, 4)
#
# def decorator(func):
#     def decorated(a, b):
#         print('사각형 : ')
#         func(a, b)
#
#     return decorated
#
# @decorator
# def square(a, b):
#     while True:
#         if a < 0 or b < 0:
#             print('Error')
#         else :
#             break
#     c = a * b
#     return c
#
#
# square(3, 4)


def check_integer(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            return func(width, height)
        else:
            raise ValueError('input positive int')
    return decorated


@check_integer
def square(w, h):
    b = w * h
    return b

@check_integer
def triangle(w, h):
    c = (w * h) / 2
    return c


square(5, 6)
triangle(8, 5)