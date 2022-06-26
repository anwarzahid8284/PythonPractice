class Python:
    def method(self):
        print("Hell Python")


py = Python()

print(type(py))
print(py.method())
print(Python.method(py))
