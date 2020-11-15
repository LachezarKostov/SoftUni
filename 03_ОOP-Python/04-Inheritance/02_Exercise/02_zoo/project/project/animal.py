class Animal(object):
    __name: str

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name
