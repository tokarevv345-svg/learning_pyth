list = []
n = 0
num = 1
n = input('введите количестно эллементов списка: ')
while True:
    try:
        n = int(n)
        break
    except ValueError:
        n = input('введите число! :')
while True:
    if (num - n) == 1:
        break
    else:
        print('Введите эллемент списка №', end = "")
        print(num, ":")
        list.append(input())
        num += 1
print('ваш список:')
for all in list:
    print(all)


