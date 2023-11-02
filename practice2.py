class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y


    @staticmethod
    def subtract(x, y):
        return x - y


    @staticmethod
    def multiply(x, y):
        return x * y


    @staticmethod
    def divide(x, y):
        if y !=0:
            return x / y

        else:
            return "Division by zero not allowed"                


print("Addition", MathUtils.add(7,9))
print("Subtraction", MathUtils.subtract(2,3))
print("Multiplication", MathUtils.multiply(9,4))
print("Division", MathUtils.divide(30, 3))