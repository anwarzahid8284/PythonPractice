class Python:
    clsVaraible = "Hi Python"

    def __init__(self):
        self.first = 10
        self.second = 15

    def avg(self):
        return (self.first + self.second) / 2

    def avg1(cls):
        return cls.clsVaraible


p1 = Python()
p2 = Python()


print(p1.avg())
print(p2.avg1())
