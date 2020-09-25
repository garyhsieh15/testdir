
class MyCalClass:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    def calc_add1(self, a, b):
        return a + b

    def calc_add2(self):
        return self.x + self.y

    #def calc_mutli(self, a, b):
    def calc_mutli(self, a, b):
        return a * b

    def calc_print(self, a):
        print("a value:", a)
        print("self.y value:", self.y)

def show_me_the_money():
    print("enter show me the money")

class_ex_a = 11


if __name__ == "__main__":

    instance_1 = MyCalClass(1, 2)
    instance_2 = MyCalClass(5, 10)

    print("instance_1.calc_add1:", instance_1.calc_add1(5, 3))
    print("instance_1.calc_add2:", instance_1.calc_add2())
    print("instance_1.mutli:", instance_1.calc_mutli(2, 4))
    instance_1.calc_print(5)

