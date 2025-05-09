class Bank:
    bank_name = "OldBank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
Bank.change_bank_name("NewBank")
print(b1.bank_name, b2.bank_name)
