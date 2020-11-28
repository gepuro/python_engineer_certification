class Person:
    def eat(self, food):
        print(f"{food}を食べた")

    def sleep(self):
        print("寝ます")


class Man(Person):
    sex = "man"


class Woman(Person):
    sex = "woman"
