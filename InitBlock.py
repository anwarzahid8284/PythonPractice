class HiPython:
    def __init__(self, languageName, languageConcept):
        self.langName = languageName
        self.langConcept = languageConcept

    def method1(self):
        print("Hia this is " + self.langName + " with " + self.langConcept)


hiPython1 = HiPython('Python', 'Object Oriented')
hiPython1.method1()
