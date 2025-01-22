## We can have multiple classes where each class implements same methods and variables in different way.

class India:
    def capital(self):
        print("New Delhi")

class Japan:
    def capital(self):
        print("Tokyo")

obj1 = India()
obj2 = Japan()
obj1.capital()
obj2.capital()