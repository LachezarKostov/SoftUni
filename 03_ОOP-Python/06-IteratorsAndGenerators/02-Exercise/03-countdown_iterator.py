class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.__current_count = count

    def __iter__(self):
        self.__current_count = self.count
        return self

    def __next__(self):
        val, self.__current_count = self.__current_count, self.__current_count - 1
        if val == -1:
            raise StopIteration
        return val

