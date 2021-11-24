

class ChessBoardNotFound(Exception):
    """
    Raised when chessboard is not found.

    :param variable_name: name of varaible which is returned
    """
    def __init__(self, varaible_name) -> None:
        self.message = "Chessboard is not found, {} are not avialbe.".format(varaible_name)
        super().__init__(self.message)



class ScreenNotBeFound(Exception):
    """ Raised when can not be found. """
    def __init__(self) -> None:
        self.message = "Screen can not be found, check PC properties."
        super().__init__()


class IndexOutOfChessBoard(Exception):
    """ Raised when something went wrong with scaling the chessboard. """
    def __init__(self) -> None:
        self.message = "Something went wrong with scaling the chessboard. Resize the chessboard by shortcut: \"ctrl +\" or \"ctrl -\""
        super().__init__()
