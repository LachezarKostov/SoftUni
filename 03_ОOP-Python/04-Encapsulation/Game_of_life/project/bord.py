from typing import List


class Bord:
    _BORD_WIDTH = 10
    _BORD_HIGH = 10

    __NO_CELL = False
    __CELL = True
    __DISPLAY_VALUES = {
        __NO_CELL: ".",
        __CELL: "X",
    }

    __bord = List[List[bool]]

    def __init__(self):
        self.__bord = [[self.__NO_CELL
                        for col in range(self._BORD_WIDTH)]
                       for row in range(self._BORD_HIGH)]

    def next_generation(self) -> None:
        for row_idx, row in enumerate(self.__bord):
            for col_idx, cell in enumerate(row):
                neighbours = self._get_neighbours(row_idx, col_idx)
                if neighbours == 3 or (cell and neighbours == 2):
                    self.spawn_cell(row_idx, col_idx)
                else:
                    self.kill_cell(row_idx, col_idx)

    def _get_neighbours(self, row, col):
        neighbours = 0

        if col + 1 < self._BORD_WIDTH:
            neighbours += int(self.__bord[row][col+1])

        if col - 1 >= 0:
            neighbours += int(self.__bord[row][col-1])

        if row + 1 < self._BORD_HIGH:
            neighbours += int(self.__bord[row + 1][col])

        if row - 1 > 0:
            neighbours += int(self.__bord[row - 1][col])

        return neighbours


    @classmethod
    def from_string(cls, string_repr: str) -> "Board":
        bord = Bord()
        rows = string_repr.strip("\n \t").split("\n")

        for row_idx, row in enumerate(rows):
            for col_idx, cell_repr in enumerate(row.strip()):
                if cell_repr == "x":
                    bord.spawn_cell(row_idx,col_idx)
        return bord

    def spawn_cell(self, row, col):
        self.__bord[row][col] = self.__CELL

    def kill_cell(self, row, col):
        self.__bord[row][col] = self.__NO_CELL

    def __str__(self) -> str:
        rows = [" ".join(self.__DISPLAY_VALUES[col] for col in row) for row in self.__bord]
        return "\n".join(rows)
