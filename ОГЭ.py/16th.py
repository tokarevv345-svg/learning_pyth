# list = []
# list_check = []
# count = int(input("введите количество чисел (до 1000, обязательно в составе цифры 4): "))
# while (inp_err := True) != False:
#     if count > 0 and count < 1001:
#         break
#     else:
#         count = int(input("введите количество чисел (до 1000)"))
#         inp_err = True
# whilepoint = count
# def f(count_inp):
#     global list
#     global list_added
#     while count_inp != whilepoint:
#         print(f"введите число №{count_inp + 1}")
#         list_added = int(input())
#         if list_added > 30000:
#             print("число больше 30000, введите пожалуйста число меньше")
#         else:
#                 list.append(list_added)
#                 count_inp += 1

# f(0)
# print(list)
# list_check = list.copy()
# error = True
# while error != False:
#     endP = count
#     for w in range(0, count):
#         list_check[w] = list[w]
#         list_check[w] = str(list_check[w])
#         if int(list_check[w][-1]) == 4:
#             error = False
#     if error == True:
#         print("в списке нет числа, кончающегося на 4")
#         list = []
#         f(0)
#         print(list)

                
                

# reverse = []
# nums = []
# list.sort()

# for i in range(0, count):
#     reverse.append(str(list[i]))
#     if int(reverse[i][-1]) == 4:
#         nums.append(reverse[i])

# print("------------------------------------")
# print("овтет:", nums[0])


#-------------------------------------------------------------------------------------------------------------

# list = []
# a = int(input())
# max = 30000
# for i in range(a):
#     num = int(input())
#     if num % 10 == 4 and num < max:
#         list.append(num)

# print(min(list))
        

#---------------------------------------------------------------------------------------------------------------

# Напишите программу, которая в последовательности натуральных чисел определяет количество однозначных чисел,
# кратных 3. Программа получает на вход натуральные числа, количество введенных чисел неизвестно,
# последовательность чисел заканчивается 0 (0  — признак окончания ввода, не входит в последовательность).
# Количество чисел 1000. Введенные числа не превышают 30 000. 
# Программа должна вывести одно число: количество однозначных чисел, кратных 3.

# a = None
# count = 0
# list = []
# while count != 1000:
#     a = int(input())
#     if a == 0:
#         break
#     if a < 10 and a % 3 == 0:
#         list.append(a)
#     count += 1
# print(len(list))
    
#-------------------------------------------------------------------------------------------------------------
# lista = []
# x = 0
# while (count := 0) != 1000:
#     a = int(input())
#     if a == 0:
#         break
#     lista.append(a)
#     if a % 2 == 0:
#         x = x + a
    
# print(f"кол-во : {len(lista)}")
# print(f'сумма четных: {x}')

