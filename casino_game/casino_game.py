# import random
# import colorama
# slots = ["🍒", "🍇", 7]
# positions = ["🍒", "🍇", 7]
# win = False
# attempt = 0
# print("нажмите \"Enter\" чтобы крутить рулетку ", end = "")
# while win != True:
#     input()
#     attempt += 1
#     slots = random.choices(positions, k=3)
#     print(slots)
#     if slots[0] == slots[1] == slots[2]:
#         print("вы победили!")
#         print(f"ваше кол-во попыток: {attempt}")
#         win = True
#     else:
#         win = False

#---------------------------------------------------------------------------------

import random
from colorama import Fore, Style
EndColor = Style.RESET_ALL
slots = ["🍒", "🍇", 7]
positions = ["🍒", "🍇", 7]
win = False
attempt = 0
print(Fore.YELLOW + "нажмите \"Enter\" чтобы крутить рулетку ", end = "" + EndColor)
while win != True:
    input()
    attempt += 1
    slots = random.choices(positions, k=3)
    print(slots)
    if len(set(slots)) == 1:
        print(Fore.GREEN + "вы победили!" + EndColor)
        print(f"ваше кол-во попыток: {attempt}")
        win = True
    else:
        win = False

