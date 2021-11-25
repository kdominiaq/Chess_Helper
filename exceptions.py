

class ChessBoardNotFound(Exception):
    """ Raised when chessboard is not found. """
    def __init__(self) -> None:
        self.message = "Chessboard is not found."
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

class LastMoveNotFound(Exception):
    """ Raised when any move has been done, return the last move is impossible, because any move hasn't been done"""
    def __init__(self) -> None:
        self.message = "Return the last move is impossible, because any move hasn't been done"
        super().__init__()