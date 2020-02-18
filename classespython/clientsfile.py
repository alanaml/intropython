class Clients:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def print_first_contact(self):
        print(f"Hello, {self.name} your weight is {self.weight} and your are {self.age} years old.\n"
              f"We are going to work with your weight, height and time")

    def imc(self):
        imc_result = self.weight / (self.height * self.height)
        # low weight
        if imc_result < 18:
            print(f"Your IMC is {round(imc_result, 2)}, your weight is to low, be careful")
        # regular weight
        elif imc_result < 25:
            print(f"Your IMC is {round(imc_result, 2)}")
        # high weight
        else:
            print(f"Your IMC is {round(imc_result, 2)},your weight is to high, be careful")


cliente01 = Clients("Alana Lima", 25, 40, 1.61)
cliente01.print_first_contact()
cliente01.imc()
