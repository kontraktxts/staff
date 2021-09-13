import matplotlib.pyplot as plt

class Controller:

    def isOdd(self, number):
        return True if number % 2 == 1 else False

    def invalidInput(self, number):
        return True if number <= 1 else False    

controller = Controller()

another_turn = True

while another_turn:

    number = int(input("Zadejte číslo větší než 1:"))

    while controller.invalidInput(number):
        number = int(input("Zadejte číslo znovu:"))


    xpoints = []
    ypoints = []
    n = 1

    while number != 1:
        xpoints.append(n)
        if controller.isOdd(number):
            number = 3*number + 1
        else:
            number = number / 2   

        print(number) 
        ypoints.append(number)
        n += 1

    print("Počet operací {}.".format(n))

    plt.plot(xpoints, ypoints)
    plt.show()

    another = input("Chcete pokračovat y/n?:")
    if another == "y":
        another_turn = True
    else:
        another_turn = False

