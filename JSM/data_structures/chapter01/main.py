class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


best = Student('Lee', 101)
print(best.get_name())
print(best.get_id())


a = []
b = [None] * 10
c = [40, 10, 70, 60]
print(c[0])
print(c[-1])
c.pop()
c.pop(0)
c.append(90)
print(len(c))
