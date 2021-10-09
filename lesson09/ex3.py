class Worker:
    def __init__(self, name, surname, position, *income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': income[0],
                         'bonus': income[1]
                         }

    def salary(self):
        return self.__income

    def full_name(self):
        return self.name, self.surname

    def info(self):
        print(self.name, self.surname, self.position, self.__income)


class Position(Worker):
    def __init__(self, name, surname, position, *income):
        super().__init__(name, surname, position, *income)

    def get_full_name(self):
        print(f'{super().full_name()[0]} {super().full_name()[1]}')

    def get_total_income(self):
        print(f'Salary: {super().salary().get("wage") + super().salary().get("bonus")}')


employee_1 = Position('Иван', 'Петров', 'электрик', 31000, 3000)
employee_1.get_full_name()
employee_1.get_total_income()

employee_2 = Position('Петр', 'Иванов', 'инженер', 110000, 40000)
employee_2.get_full_name()
employee_2.get_total_income()