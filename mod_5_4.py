class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        instance = super().__new__(cls)
        return instance
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to (self,new_floor):
        if new_floor in range(1, self.number_of_floors + 1):
            return new_floor
        else:
            return "Такого этажа не существует"
    def __del__(self):
        print(F"{self.name} снесён, но он останется в истории")
h1 = House("ЖК Эльбрус", 10)
print(House.houses_history)
h2 = House("ЖК Акация", 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
input()



