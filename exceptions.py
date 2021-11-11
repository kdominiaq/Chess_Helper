

class ChessBoardNotFound(Exception):
    def __init__(self, varaible_name) -> None:
        """
        Raised when chessboard is not found.

        :param variable_name: name of varaible which is returned
        """
        self.message = "Chessboard is not found, {} are not avialbe.".format(varaible_name)
        super().__init__(self.message)



class ScreenNotBeFound(Exception):
    def __init__(self) -> None:
        self.message = "Screen can not be found, check PC properties."
        super().__init__()