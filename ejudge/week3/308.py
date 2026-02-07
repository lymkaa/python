class Account:
    def __init__(self, owner, b):
        self.owner = owner
        self.balance = b

    def deposit(self, a):
        self.balance += a

    def withdraw(self, a):
        if a > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= a
            return self.balance


if __name__ == "__main__":
    b, a = map(int, input().split())
    account = Account("Owner", b)
    result = account.withdraw(a)
    print(result)
