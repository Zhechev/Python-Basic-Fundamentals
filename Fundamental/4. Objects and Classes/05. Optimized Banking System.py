class BankAccount:
    name = None
    bank = None
    balance = None

    def __init__(self, name, bank, balance):
        self.set_name(name)
        self.set_bank(bank)
        self.set_balance(balance)

    def set_name(self, name):
        self.name = name

    def set_bank(self, bank):
        self.bank = bank

    def set_balance(self, balance):
        self.balance = balance


accounts = []

input_row = input()

while input_row != "end":
    data = input_row.split(' | ')
    bank = data[0]
    account_name = data[1]
    balance = float(data[2])

    account = BankAccount(account_name, bank, balance)
    accounts.append(account)

    input_row = input()

accounts = sorted(accounts, key=lambda obj: (-obj.balance, obj.bank))

for account in accounts:
    print(f"{account.name} -> {account.balance:.2f} ({account.bank})")


