# # print("x y z w ")
# # for x in range(2):
# #     for y in range(2):
# #         for z in range(2):
# #             for w in range(2):
# #                 if (x or y) and (not(y == z)) and (not w):
# #                     print(x, y, z, w)

# #----------------------------------------------------------------------------------------

# # print("x y z w")
# # for x in range(2):
# #     for y in range(2):
# #         for z in range(2):
# #             for w in range(2):
# #                 if not (((x <= z) <= w) or (not y)):
# #                     print(x, y, z, w)

# # y z x w
# # 1 1 1 0
# # 1 0 0 0
# # 1 1 0 0

# #------------------------------------------------------------------------------------------
# # print("x y z w")
# # for x in range(2):
# #     for y in range(2):
# #         for z in range(2):
# #             for w in range(2):
# #                 if (( x == y) <= ((not z) or w )) == (not((w <= x) or (y <= z))):
# #                     print(x, y, z, w)

# #вывод
# # x y z w
# # 0 0 1 0
# # 0 1 0 1
# # 1 1 1 0

# #таблица
# # w z y x
# # 0 1 1 1
# # 1 0 1 0
# # 0 1 0 0

# # from itertools import *
# # def f(x, y, z, w):
# #     return(( x == y) <= ((not z) or w )) == (not((w <= x) or (y <= z)))
# # for a, b, e, g, h in product([0, 1], repeat=5):
# #     table = (
# #         (0, 1, a, b, 1),
# #         (e ,g, 1, 0, 1),
# #         (0, h, 0, 0, 1)
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations("xyzw", r=4):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)


# # from itertools import *

# # def f(w, x, y, z):
# #     return ((x or y) <= z) or (y == w) or z

# # for a, b, c, d in product([0, 1], repeat=4):
# #     table = (
# #         (0, 1, a, b, 0),
# #         (1, c, 1, 0, 0),
# #         (d, 1, 1, 0, 0)
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations("wxyz", r=4):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)
    

# # from itertools import product, permutations

# # def f(x, y, w, z):
# #     return ((x == y) <= ((not z) or w)) == (not((w <= x) or (y <= z)))
# # for a, b, c, d, e in product([0,1], repeat=5):
# #     table = (
# #         (0, 1, a, b, 1),
# #         (c, d, 1, 0, 1),
# #         (0, e, 0, 0, 1),
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations("xywz", r=4):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)

# # from itertools import permutations, product

# # def f(x, w, y, z):
# #     return (not x) or y and z or y and (not w) or (not z) and (not w)

# # for i in product([0,1]):
# #     table = (
# #         (0, 0, 1, 1, 0),
# #         (0, 1, 0, 1, 0),
# #         (0, 1, 1, 1, 0),
# #         (1, 1, 0, 1, 0),
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations('xwyz', r=4):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)

# # from itertools import product, permutations

# # def f(x, y, w, z):
# #     return (not x) or (not y) and (not z) or (not z) and (not w) or (not y) and w

# # for i in product([0,1]):
# #     table = (
# #         (1, 0, 1, 1, 0),
# #         (1, 1, 0, 0, 0),
# #         (1, 1, 1, 0, 0),
# #         (1, 1, 1, 1, 0)
# #     )

# #     if len(table) == len(set(table)):
# #         for p in permutations('xywz'):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)









# # from itertools import product, permutations

# # def f(x, y, w, z):
# #     return (x or ((not y) or z or (not w)) and (y or (not z)))

# # for i in product([0,1]):
# #     table = (
# #         (0, 0, 1, 0, 0),
# #         (1, 0, 0, 1, 0),
# #         (1, 0, 1, 0, 0),
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations('xywz', r=4):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)



# # from itertools import product, permutations

# # def f(x, y, w, z):
# #     return (x == (w or y)) or ((w <= z) and (y <= w))

# # for a, b, c, d, e, g, h in product([0,1], repeat=7):
# #     table = (
# #         (1, a, b, 1, 0),
# #         (c, d, e, 1, 0),
# #         (1, g, 1, h, 0),
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations('xywz', r=4):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)







# # from itertools import product, permutations

# # def f(x, y, w, z):
# #     return x and (y and z or y and (not w) or (not w) and (not z))

# # for i in product([0,1]):
# #     table = (
# #         (0, 0, 0, 1, 1),
# #         (1, 0, 0, 1, 1),
# #         (1, 0, 1, 1, 1),
# #         (1, 1, 1, 1, 1),
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations('xywz'):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)




# # from itertools import permutations, product

# # def f(x, y, w, z):
# #     return ((x and (not y)) == (z or (not w))) <= ( x and z)

# # for a, b, c, d, e, g in product([0,1], repeat=6):
# #     table = (
# #         (1, a, 1, 1, 0),
# #         (1, b, 1, c, 0),
# #         (d, e, 1, g, 0),
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations('xywz', r=4):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)



# # from itertools import permutations, product
# # def f(x, y, w, z):
# #     return ((x <= y) or (y == w)) and ((x or z) == w)

# # for a, b, c, d in product([0,1], repeat=4):
# #     table = (
# #         (1, 0, 0, 1, 1),
# #         (0, a, b, 1, 1),
# #         (c, 1, 0, d, 1),
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations('xywz', r=4):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)

# # print("x y z")
# # for x in range(2):
# #     for y in range(2):
# #         for z in range(2):
# #             if not( ((not x) or z) and ((not x) or (not y) or (not z)) ):
# #                 print(x, y, z)
    



# # from itertools import permutations, product

# # def f(x, y,w,z):
# #     return (x == (w or y)) or ((w <= z) and (y <= w))

# # for a, b, c, d, e, g, h in product([0,1], repeat=7):
# #     table = (
# #         (1,a,b,1,0),
# #         (c,d,e,1,0),
# #         (1,g,1,h,0),
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations("xywz",r=4):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)




# # from itertools import *

# # def f (x,y,w,z):
# #     return (y <= z) and (not (y or w) <= (z and x))

# # for a,b,c,d,e in product([0,1], repeat=5):
# #     table = (
# #         (1,1,a,1,1),
# #         (b,1,1,c,1),
# #         (1,1,d,e,1),
# #     )       
# #     if len(table) == len(set(table)):
# #         for p in permutations('xywz'):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)


# #-----------------------------------------------------------------------------


# # from itertools import product, permutations

# # def f(x,y,w,z):
# #     return (x == (not y)) <= ((z <= (not w) and (w <= y)))

# # for a,b,c,d,e in product([0,1], repeat=5):
# #     table = (
# #         (1,1,0,1,1),
# #         (0,a,0,b,0),
# #         (c,d,e,0,0),
# #     )
# #     if len(table) == len(set(table)):
# #         for p in permutations("xywz"):
# #             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
# #                 print(*p)



# from itertools import permutations, product

# def f(x,y,w,z):
#     return ((x <= y) and (z or w)) <= ((x == w) or (y and (not z)))

# for a,b,c,d,e in product([0,1], repeat=5):
#     table = (
#         (0,0,a,0,0),
#         (1,b,1,1,0),
#         (0,c,d,e,0),
#     )
#     if len(table) == len(set(table)):
#         for p in permutations('xywz'):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)


#-------------------------------------------------------------------------------------


# from itertools import product, permutations

# def f(x,y,w,z):
#     return (x or y) and (not(y == z)) and (not w)

# for a,b,c,d in product([0,1], repeat=4):
#     table = (
#         (a,1,b,1,1),
#         (0,0,1,c,1),
#         (0,d,1,1,1),
#     )
#     if len(table) == len(set(table)):
#         for p in permutations('xywz'):
#             if all(f(**dict(zip(p,line))) == line[-1] for line in table):
#                 print(*p)

# from itertools import permutations, product

# def f(a,b,c,d):
#   return (a <= b) and (b <= c) and (c <= d)

# for a,b in product([0,1], repeat=2):
#     table = (
#     (0,a,1,0,1),
#     (0,b,1,0,1),
#     (0,1,1,1,1),
#     )
#     if len(table) == len(set(table)):
#         for p in permutations("abcd"):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
#                 print(*p)


# from itertools import permutations, product

# def f(x,y,w,z):
#     return (not (z <= x) and (w or y) and (not (w == x)))

# for a,b,c,d,e,g in product([0,1], repeat=6):
#     table = (
#         (a,b,c,1,0),
#         (0,0,d,e,0),
#         (g,1,1,1,0),
#     )
#     if len(table) == len(set(table)):
#         for p in permutations('xywz'):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
#                 print(*p)
  

count = []
from itertools import permutations, product

def f(x,y,w,z):
    return (not (not (x <= (not w))) and z )   and (not (w <= z)) and (x <= (not z))

for a, b, c, d, e in product([0,1], repeat=5):
    table = (
        (1,0,a,0,1),
        (1,0,b,c,0),
        (d,1,e,1,0),
    )
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                count.append(p)

print(len(set(count)))
