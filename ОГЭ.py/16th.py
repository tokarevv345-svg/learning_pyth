list = []
list_check = []
count = int(input("введите количество чисел (до 1000, обязательно в составе цифры 4): "))
while (inp_err := True) != False:
    if count > 0 and count < 1001:
        break
    else:
        count = int(input("введите количество чисел (до 1000)"))
        inp_err = True
whilepoint = count
def f(count_inp):
    global list
    global list_added
    while count_inp != whilepoint:
        print(f"введите число №{count_inp + 1}")
        list_added = int(input())
        if list_added > 30000:
            print("число больше 30000, введите пожалуйста число меньше")
        else:
                list.append(list_added)
                count_inp += 1

f(0)
print(list)
list_check = list.copy()
error = True
while error != False:
    endP = count
    for w in range(0, count):
        list_check[w] = list[w]
        list_check[w] = str(list_check[w])
        if int(list_check[w][-1]) == 4:
            error = False
    if error == True:
        print("в списке нет числа, кончающегося на 4")
        list = []
        f(0)
        print(list)

                
                

reverse = []
nums = []
list.sort()

for i in range(0, count):
    reverse.append(str(list[i]))
    if int(reverse[i][-1]) == 4:
        nums.append(reverse[i])

print("------------------------------------")
print("овтет:", nums[0])
