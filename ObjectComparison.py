class Python:
    def __init__(self):
        self.name = "Haroon"
        self.desi = "Designer"

    def compare(self, secondObj):
        if self.desi == secondObj.desi:
            return True
        else:
            return False


py1 = Python()
py1.name = "Zahid"
py2 = Python()

if py1.compare(py2):
    print("object are same")
else:
    print("object are different")

print(id(py1))
print(id(py2))
