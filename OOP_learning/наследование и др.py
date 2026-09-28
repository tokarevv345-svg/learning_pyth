class city:
    willagers = None
    central = None

    def __init__(self, wilagers = None, central = None):
        self.wilagers = wilagers
        self.central = central

    def get_inf(self):
        print(f"население: {self.wilagers}, гланая улица : {self.central}" )



bgd = city(100000, "родина")
msc = city("1.000.000", "китай город" )

class moscow(city):
    scyscrappers = None
    
    def __init__(self, wilagers = None, scyscrappers = None):
        self.wilagers = wilagers
        self.scyscrappers = scyscrappers

    def get_inf(self):
        print(self.wilagers, self.scyscrappers)

mosc = moscow(5, 1000000)

mosc.get_inf()