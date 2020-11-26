class take_skip():
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        val = self.current
        self.current += self.step
        gennerated_so_fat = (val / self.step) + 1
        if gennerated_so_fat > self.count:
            raise StopIteration
        return val
