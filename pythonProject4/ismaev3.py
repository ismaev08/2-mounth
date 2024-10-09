class Computer:
    def _init_(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory


    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory


    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_memory(self, memory):
        self.__memory = memory


    def make_computations(self):
        result = self.__cpu + self.__memory
        return result


    def __str__(self):
        return f"Computer: CPU={self.__cpu}, Memory={self.__memory}"

class Phone:
    def _init_(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list


    def get_sim_cards_list(self):
        return self.__sim_cards_list


    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        sim_card = f"сим-карты-{sim_card_number}"
        print(f"Идет звонок на номер {call_to_number} с {sim_card} - Beeline")


    def _str_(self):
        return f"Phone: Sim Cards={self.__sim_cards_list}"

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer._init_(self, cpu, memory)
        Phone._init_(self, sim_cards_list)


    def use_gps(self, location):
        print(f"Построение маршрута до {location}")


    def _str_(self):
        return (f"SmartPhone: CPU={self.get_cpu()}, Memory={self.get_memory()}, "
                f"Sim Cards={self.get_sim_cards_list()}")


computer = Computer("Intel i7", 16)
phone = Phone(["Beeline", "Megacom", "O!"])

smartphone1 = SmartPhone("Snapdragon 855", 8, ["MTS", "Tele2"])

smartphone2 = SmartPhone("Exynos 990", 12, ["T-Mobile", "Verizon"])


print(computer)
print(phone)
print(smartphone1)
print(smartphone2)


print("Вычисления на компьютере:", computer.make_computations())

phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Дом")


print(computer == smartphone1)
print(smartphone1 < smartphone2)