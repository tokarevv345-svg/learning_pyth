print("Это-калькулятор! Для остановки напиши 'стоп'")
while True:
    a = input("введите первое число:")
    if a == "стоп":
        quit()
    while True:
        try:
            if a == "стоп":
                quit()
            a = float(a)
            break
        except:
            a = input("ОШИБКА! Введите число:")            
    b = input("введите операцию:")
    if b == "стоп":
        quit()
    while b not in [ "+", "-", "*", "/", "^"]:
        b = input("ОШИБКА! Введите + или - или * или / или ^ :")
    if b == "стоп":
        quit()
    c = input("введите второе число:")
    if c == "стоп":
        quit()
    while True:
        try:
            if c == "стоп":
                quit()
            c = float(c)
            break
        except:
            c = input("ОШИБКА! Введите число:")
    if b == "+":
        print(a + c)
    elif b == "-":
        print(a - c)
    elif b == "*":
        print(a * c)
    elif b == "/":
        if c == 0:
            print("ОШИБКА! На ноль делить нельзя")
        else:
            print(a / c)
    elif b == "^":
        print(a ** c)

    
