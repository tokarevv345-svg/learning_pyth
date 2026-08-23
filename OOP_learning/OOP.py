class dota_hero:
    name = None
    attribute = None 
    pose = None

    def dataset(self, name, attribute, pose):
        self.name = name   #self - обращение к классу
        self.attribute = attribute
        self.pose = pose

    def dataget(self):
        print(f"Hero name: {self.name}")
        print(f"Hero attribute: {self.attribute}")
        print(f"Hero pose: {self.pose}")

pudge = dota_hero()
pudge.name = "Pudge"
pudge.attribute = "strenght"
pudge.pose = 1

arc = dota_hero()
arc.name = "Arc Warden"
arc.attribute = "universal"
arc.pose = 2


puck = dota_hero()
puck.dataset("puck", 'int', 2)

# print(arc.name)
# print(pudge.name)
# print("")
# puck.dataget()


#------------------------------------------------------------------------------------------------------------------

class phone:
    name = None
    ram = None
    price = None

    def __init__(self, name, ram, price):
        self.name = name
        self.ram = ram
        self.price = price

    def dataget(self):
        print(f"Phone name: {self.name}")
        print(f"Phone ram: {self.ram}")
        print(f"Phone price: {self.price}")

phone1 = phone("Iphone 11", 8, 40000)

# phone1.dataget()





#--------------------------------------------------------------------------------------------------------------

class boys:
    name = None
    age = None
    sport = None

    def __init__(self, name, age, sport):
        self.name = name
        self.age = age
        self.sport = sport

    def dataget(self):
        print(f"Name: {self.name}")     
        print(f"Age: {self.age}")
        print(f"Sport: {self.sport}")

boy1 = boys("Арсюшка", 23, "анонизм и прокрастинаторство")
boy2 = boys("Шинкарев", 16, "неполучение секса от своей телки")
# boy1.dataget()
# boy2.dataget()


#----------------------------------------------------------------------------------------------------------------


class devolper:
    name = None
    lang = None
    ai = None

    def __init__(self, name = None, lang = None, ai = "своих знаний"):
        self.name = name
        self.lang = lang
        self.ai = ai
        print(f"разваботчик по имени {self.name} пишет на языке {self.lang} при помощи {self.ai}")
            
# print("~")
# dev1 = devolper("Igor", "Python")
# print("~")
# dev2 = devolper("Anton", "C++", "Codex")
# print("~")
# dev3 = devolper("Yurec", "Java Script", "Claude")
# print("~")

#--------------------------------------------------------------------------

class bus:
    num = None
    EndP = None
    pidor = None

    def __init__(self, num = None, EndP = None, pidor = None):
        self.num = num
        self.EndP = EndP
        self.pidor = pidor

    def inf(self):
        print(f"автобус номер {self.num} едет до {self.EndP}, а его водитель {self.pidor} ")

first = bus(112, "северного", "пидорас гнойный")

second = bus(15, "секса", "норм мужик")

third = bus(127, "хуй его знает", "хуй знает кто")

# first.inf()
# print("~")
# second.inf()
# print("~")
# third.inf()

numbus = input("напиши номер автобуса: (15/112/127)")

error = True
while error != False:
    try:
        numbus = float(numbus)
        if numbus not in [112, 15, 127]:
            print("такого автобуса я не знаю")
            error = True
            numbus = input("напиши номер автобуса: ")
        if numbus == 112:
            first.inf()
            error = False
        elif numbus == 15:
            second.inf()
            error = False
        elif numbus == 127:
            third.inf()
            error = False
    except:
        print("че за хуйню ты написал?")
        numbus = input("напиши номер автобуса: ")



