class Encoder:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __result(self):
        return self.__a / self.__b * 0.9
    def get_result(self):
        return self.__result()


en = Encoder(3, 6)
print(en.get_result())

