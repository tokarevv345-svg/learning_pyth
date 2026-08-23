a = 0
print("теперь эта ебень рисует письку указанного размера")
print("какого размера нужна писька? (число)")
while a != 1:
    try:
        size = int(input())
        a = 1
    except ValueError:
        print("это не число, я не могу нарисовать письку")
print("c", end = "")
print(("=" * size), end = "")
print("з")