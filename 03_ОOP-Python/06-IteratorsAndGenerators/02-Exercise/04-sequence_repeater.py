class sequence_repeat:
    def __init__(self, seq, repeat_for):
        self.__seq = seq
        self.__repeat_for = repeat_for
        self.__idx = 0

    def __iter__(self):
        self.__idx = 0
        return self

    def __next__(self):
        idx, self.__idx = self.__idx, self.__idx + 1
        if idx == self.__repeat_for:
            raise StopIteration
        return self.__seq[idx % len(self.__seq)]
