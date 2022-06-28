class Python:
    favorite = "Emerging Technologies"

    def __init__(self):
        # instance variable
        self.lang = "Python"
        self.int = "DataScience"


py = Python()
py1 = Python()
Python.favorite = "Yes"

print(py.lang, py1.lang, py.favorite, py1.favorite)
