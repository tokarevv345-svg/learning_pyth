a = float(input("введите первое число:"))
b = input("введите операцию:")
while b not in [ "+", "-", "*", "/", "^"]:
    b = input("неизвестная операция, введите снова:")
c = float(input("введите второе число:"))
if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    if c == 0:
        print("на ноль делить нельзя")
    else:
        print(a / c)
elif b == "^":
    print(a ** c)
    
