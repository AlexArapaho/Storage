# комиссия при снятии задана переменой comm, в данном случае 5% от суммы снятия
# , списание комиссии осуществляется при снятии методом withdraw_money

class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"
    comm = 0.05 # комиссия при снятии

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f"счёт номер {self.num} , принадлежащий {self.surname} , был открыт")
        print("*" * 50)

    def __del__(self):
        print()
        print("*"*50)
        print(f"Счёт {self.num} , принадлежащий {self.surname} , был закрыт")

    @staticmethod
    def convert(value, rate):
        return value*rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_euro = rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счёта {usd_val}{self.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_euro)
        print(f"Состояние счёта {eur_val}{self.suffix_eur}")

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print("Проценты начислены!")
        self.print_balance()

    def withdraw_money(self, val):
        if val + val*Account.comm > self.value:
            print(f"К сожалению у вас нет {val}{Account.suffix}")
        else:
            self.value -= val + val*Account.comm
            print(f"{val}{Account.suffix} успешно снято, комиссия за снятие {Account.comm*val}{Account.suffix}!")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val}{Account.suffix} успешно внесено!")
        self.print_balance()

    def print_balance(self):
            print(f"Текущий баланс {self.value}{Account.suffix}")

    def print_info(self):
            print("Информация о счёте")
            print("-" * 20)
            print(f"#{self.num}")
            print(f"Владелец {self.surname}")
            self.print_balance()
            print(f"Процент {self.percent:0%}")
            print("-" * 20)



acc = Account("4848", "Иванов", 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.set_usd_rate(2)
acc.convert_to_usd()
acc.set_eur_rate(3)
acc.convert_to_eur()
print()
acc.edit_owner("Дюма")
acc.print_info()
acc.add_percent()
print()
acc.withdraw_money(100)
print()
acc.withdraw_money(5000)
print()
acc.add_money(5000)