class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu * self.__memory  # Пример вычислений

    def __str__(self):
        return f"Computer(CPU: {self.__cpu}, Memory: {self.__memory})"

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __le__(self, other):
        return self.memory <= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number < 1 or sim_card_number > len(self.__sim_cards_list):
            print("Неверный номер сим-карты.")
            return
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")

    def __str__(self):
        return f"Phone(SIM Cards: {self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        return f"SmartPhone(CPU: {self.cpu}, Memory: {self.memory}, SIM Cards: {self.sim_cards_list})"


# Создание объектов
computer1 = Computer(cpu=3.2, memory=16)
phone1 = Phone(sim_cards_list=["Beeline", "MegaCom", "O!", "Altel"])
smartphone1 = SmartPhone(cpu=2.8, memory=8, sim_cards_list=["Beeline", "MegaCom"])
smartphone2 = SmartPhone(cpu=3.0, memory=12, sim_cards_list=["O!", "Altel"])

# Печать информации о созданных объектах
print(computer1)
print(phone1)
print(smartphone1)
print(smartphone2)

# Применение методов
print(computer1.make_computations())
phone1.call(1, "+996 777 99 88 11")
smartphone1.use_gps("ЦУМА")
smartphone2.call(2, "+996 555 44 33 22")

# Опробовать магические методы сравнения
print(computer1 == smartphone1)  # Сравнение по памяти
print(computer1 < smartphone2)    # Сравнение по памяти
