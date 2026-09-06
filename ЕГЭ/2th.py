# print("x y z w ")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x or y) and (not(y == z)) and (not w):
#                     print(x, y, z, w)

#----------------------------------------------------------------------------------------

# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not (((x <= z) <= w) or (not y)):
#                     print(x, y, z, w)

# y z x w
# 1 1 1 0
# 1 0 0 0
# 1 1 0 0

#------------------------------------------------------------------------------------------
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (( x == y) <= ((not z) or w )) == (not((w <= x) or (y <= z))):
#                     print(x, y, z, w)

#вывод
# x y z w
# 0 0 1 0
# 0 1 0 1
# 1 1 1 0

#таблица
# w z y x
# 0 1 1 1
# 1 0 1 0
# 0 1 0 0

# from itertools import *
# def f(x, y, z, w):
#     return(( x == y) <= ((not z) or w )) == (not((w <= x) or (y <= z)))
# for a, b, e, g, h in product([0, 1], repeat=5):
#     table = (
#         (0, 1, a, b, 1),
#         (e ,g, 1, 0, 1),
#         (0, h, 0, 0, 1)
#     )
#     if len(table) == len(set(table)):
#         for p in permutations("xyzw", r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
#                 print(*p)


# from itertools import *

# def f(w, x, y, z):
#     return ((x or y) <= z) or (y == w) or z

# for a, b, c, d in product([0, 1], repeat=4):
#     table = (
#         (0, 1, a, b, 0),
#         (1, c, 1, 0, 0),
#         (d, 1, 1, 0, 0)
#     )
#     if len(table) == len(set(table)):
#         for p in permutations("wxyz", r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
#                 print(*p)
    

# from itertools import product, permutations

# def f(x, y, w, z):
#     return ((x == y) <= ((not z) or w)) == (not((w <= x) or (y <= z)))
# for a, b, c, d, e in product([0,1], repeat=5):
#     table = (
#         (0, 1, a, b, 1),
#         (c, d, 1, 0, 1),
#         (0, e, 0, 0, 1),
#     )
#     if len(table) == len(set(table)):
#         for p in permutations("xywz", r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
#                 print(*p)

# from itertools import permutations, product

# def f(x, w, y, z):
#     return (not x) or y and z or y and (not w) or (not z) and (not w)

# for i in product([0,1]):
#     table = (
#         (0, 0, 1, 1, 0),
#         (0, 1, 0, 1, 0),
#         (0, 1, 1, 1, 0),
#         (1, 1, 0, 1, 0),
#     )
#     if len(table) == len(set(table)):
#         for p in permutations('xwyz', r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
#                 print(*p)

# from itertools import product, permutations

# def f(x, y, w, z):
#     return (not x) or (not y) and (not z) or (not z) and (not w) or (not y) and w

# for i in product([0,1]):
#     table = (
#         (1, 0, 1, 1, 0),
#         (1, 1, 0, 0, 0),
#         (1, 1, 1, 0, 0),
#         (1, 1, 1, 1, 0)
#     )

#     if len(table) == len(set(table)):
#         for p in permutations('xywz'):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
#                 print(*p)









# from itertools import product, permutations

# def f(x, y, w, z):
#     return (x or ((not y) or z or (not w)) and (y or (not z)))

# for i in product([0,1]):
#     table = (
#         (0, 0, 1, 0, 0),
#         (1, 0, 0, 1, 0),
#         (1, 0, 1, 0, 0),
#     )
#     if len(table) == len(set(table)):
#         for p in permutations('xywz', r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
#                 print(*p)



from itertools import product, permutations

def f(x, y, w, z):
    return (x == (w or y)) or ((w <= z) and (y <= w))

for a, b, c, d, e, g, h in product([0,1], repeat=7):
    table = (
        (1, a, b, 1, 0),
        (c, d, e, 1, 0),
        (1, g, 1, h, 0),
    )
    if len(table) == len(set(table)):
        for p in permutations('xywz', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)