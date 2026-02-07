class Employee:
    def __init__(self, name, bs):
        self.name = name
        self.bs = bs

    def total_salary(self):
        return float(self.bs)

class Manager(Employee):
    def __init__(self, name, bs, bp):
        super().__init__(name, bs)
        self.bp = bp

    def total_salary(self):
        return self.bs * (1 + self.bp / 100)

class Developer(Employee):
    def __init__(self, name, bs, cp):
        super().__init__(name, bs)
        self.cp = cp

    def total_salary(self):
        return self.bs + 500 * self.cp

class Intern(Employee):
    pass

if __name__ == "__main__":
    data = input().split()
    role = data[0]
    name = data[1]
    bs = int(data[2])

    if role == "Manager":
        bp = int(data[3])
        emp = Manager(name, bs, bp)
    elif role == "Developer":
        cp = int(data[3])
        emp = Developer(name, bs, cp)
    else:  
        emp = Intern(name, bs)

    total = emp.total_salary()
    print(f"Name: {emp.name}, Total: {total:.2f}")
