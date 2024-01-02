"""В проекте «Дом питомца» добавим новую услугу — электронный кошелек. Необходимо создать класс «Клиент», 
который будет содержать данные о клиентах и их финансовых операциях. О клиенте известна следующая информация: имя, 
фамилия, город, баланс. Далее сделайте вывод о клиентах в консоль в формате: «Иван Петров. Москва. Баланс: 50 руб.»"""


class Client:
    def __init__(self, fst_name, sc_name, city, balance=0):
        self.fst_name = fst_name
        self.sc_name = sc_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.fst_name} {self.sc_name}. {self.city}. Баланс: {self.balance} руб."


client_1 = Client("Aleksandr", "Zhukov", "Volgodonsk", 10500)
print(client_1)
