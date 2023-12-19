class EmployeeRecord:
    def __init__(self, n, i, r):
        self.name = n
        self.id = i
        self.pay_rate = r


rec = EmployeeRecord("Mary", 2148, 10)

print(rec.name)
print(rec.id)
print(rec.pay_rate)