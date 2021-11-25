
class ChessNotation:
    def __init__(self, _field_x, _field_y) -> None:
        """ Data of two posible oriatioation of the chessboard, white or black pieces on the bottom on the chessboard."""
        
        self._white_pieces_on_the_bottom=[{'notation': 'a1', 'position': (self._field_y * 7, self._field_x * 0)},
                                         {'notation': 'a2', 'position': (self._field_y * 6, self._field_x * 0)},
                                         {'notation': 'a3', 'position': (self._field_y * 5, self._field_x * 0)},
                                         {'notation': 'a4', 'position': (self._field_y * 4, self._field_x * 0)},
                                         {'notation': 'a5', 'position': (self._field_y * 3, self._field_x * 0)},
                                         {'notation': 'a6', 'position': (self._field_y * 2, self._field_x * 0)},
                                         {'notation': 'a7', 'position': (self._field_y * 1, self._field_x * 0)},
                                         {'notation': 'a8', 'position': (self._field_y * 0, self._field_x * 0)},

                                         {'notation': 'b1', 'position': (self._field_y * 7, self._field_x * 1)},
                                         {'notation': 'b2', 'position': (self._field_y * 6, self._field_x * 1)},
                                         {'notation': 'b3', 'position': (self._field_y * 5, self._field_x * 1)},
                                         {'notation': 'b4', 'position': (self._field_y * 4, self._field_x * 1)},
                                         {'notation': 'b5', 'position': (self._field_y * 3, self._field_x * 1)},
                                         {'notation': 'b6', 'position': (self._field_y * 2, self._field_x * 1)},
                                         {'notation': 'b7', 'position': (self._field_y * 1, self._field_x * 1)},
                                         {'notation': 'b8', 'position': (self._field_y * 0, self._field_x * 1)},

                                         {'notation': 'c1', 'position': (self._field_y * 7, self._field_x * 2)},
                                         {'notation': 'c2', 'position': (self._field_y * 6, self._field_x * 2)},
                                         {'notation': 'c3', 'position': (self._field_y * 5, self._field_x * 2)},
                                         {'notation': 'c4', 'position': (self._field_y * 4, self._field_x * 2)},
                                         {'notation': 'c5', 'position': (self._field_y * 3, self._field_x * 2)},
                                         {'notation': 'c6', 'position': (self._field_y * 2, self._field_x * 2)},
                                         {'notation': 'c7', 'position': (self._field_y * 1, self._field_x * 2)},
                                         {'notation': 'c8', 'position': (self._field_y * 0, self._field_x * 2)},

                                         {'notation': 'd1', 'position': (self._field_y * 7, self._field_x * 3)},
                                         {'notation': 'd2', 'position': (self._field_y * 6, self._field_x * 3)},
                                         {'notation': 'd3', 'position': (self._field_y * 5, self._field_x * 3)},
                                         {'notation': 'd4', 'position': (self._field_y * 4, self._field_x * 3)},
                                         {'notation': 'd5', 'position': (self._field_y * 3, self._field_x * 3)},
                                         {'notation': 'd6', 'position': (self._field_y * 2, self._field_x * 3)},
                                         {'notation': 'd7', 'position': (self._field_y * 1, self._field_x * 3)},
                                         {'notation': 'd8', 'position': (self._field_y * 0, self._field_x * 3)},

                                         {'notation': 'e1', 'position': (self._field_y * 7, self._field_x * 4)},
                                         {'notation': 'e2', 'position': (self._field_y * 6, self._field_x * 4)},
                                         {'notation': 'e3', 'position': (self._field_y * 5, self._field_x * 4)},
                                         {'notation': 'e4', 'position': (self._field_y * 4, self._field_x * 4)},
                                         {'notation': 'e5', 'position': (self._field_y * 3, self._field_x * 4)},
                                         {'notation': 'e6', 'position': (self._field_y * 2, self._field_x * 4)},
                                         {'notation': 'e7', 'position': (self._field_y * 1, self._field_x * 4)},
                                         {'notation': 'e8', 'position': (self._field_y * 0, self._field_x * 4)},

                                         {'notation': 'f1', 'position': (self._field_y * 7, self._field_x * 5)},
                                         {'notation': 'f2', 'position': (self._field_y * 6, self._field_x * 5)},
                                         {'notation': 'f3', 'position': (self._field_y * 5, self._field_x * 5)},
                                         {'notation': 'f4', 'position': (self._field_y * 4, self._field_x * 5)},
                                         {'notation': 'f5', 'position': (self._field_y * 3, self._field_x * 5)},
                                         {'notation': 'f6', 'position': (self._field_y * 2, self._field_x * 5)},
                                         {'notation': 'f7', 'position': (self._field_y * 1, self._field_x * 5)},
                                         {'notation': 'f8', 'position': (self._field_y * 0, self._field_x * 5)},

                                         {'notation': 'g1', 'position': (self._field_y * 7, self._field_x * 6)},
                                         {'notation': 'g2', 'position': (self._field_y * 6, self._field_x * 6)},
                                         {'notation': 'g3', 'position': (self._field_y * 5, self._field_x * 6)},
                                         {'notation': 'g4', 'position': (self._field_y * 4, self._field_x * 6)},
                                         {'notation': 'g5', 'position': (self._field_y * 3, self._field_x * 6)},
                                         {'notation': 'g6', 'position': (self._field_y * 2, self._field_x * 6)},
                                         {'notation': 'g7', 'position': (self._field_y * 1, self._field_x * 6)},
                                         {'notation': 'g8', 'position': (self._field_y * 0, self._field_x * 6)},

                                         {'notation': 'h1', 'position': (self._field_y * 7, self._field_x * 7)},
                                         {'notation': 'h2', 'position': (self._field_y * 6, self._field_x * 7)},
                                         {'notation': 'h3', 'position': (self._field_y * 5, self._field_x * 7)},
                                         {'notation': 'h4', 'position': (self._field_y * 4, self._field_x * 7)},
                                         {'notation': 'h5', 'position': (self._field_y * 3, self._field_x * 7)},
                                         {'notation': 'h6', 'position': (self._field_y * 2, self._field_x * 7)},
                                         {'notation': 'h7', 'position': (self._field_y * 1, self._field_x * 7)},
                                         {'notation': 'h8', 'position': (self._field_y * 0, self._field_x * 7)}]


        self._black_pieces_on_the_bottom=[{'notation': 'a1', 'position': (self._field_y * 0, self._field_x * 7)},
                                         {'notation': 'a2', 'position': (self._field_y * 1, self._field_x * 7)},
                                         {'notation': 'a3', 'position': (self._field_y * 2, self._field_x * 7)},
                                         {'notation': 'a4', 'position': (self._field_y * 3, self._field_x * 7)},
                                         {'notation': 'a5', 'position': (self._field_y * 4, self._field_x * 7)},
                                         {'notation': 'a6', 'position': (self._field_y * 5, self._field_x * 7)},
                                         {'notation': 'a7', 'position': (self._field_y * 6, self._field_x * 7)},
                                         {'notation': 'a8', 'position': (self._field_y * 7, self._field_x * 7)},

                                         {'notation': 'b1', 'position': (self._field_y * 0, self._field_x * 6)},
                                         {'notation': 'b2', 'position': (self._field_y * 1, self._field_x * 6)},
                                         {'notation': 'b3', 'position': (self._field_y * 2, self._field_x * 6)},
                                         {'notation': 'b4', 'position': (self._field_y * 3, self._field_x * 6)},
                                         {'notation': 'b5', 'position': (self._field_y * 4, self._field_x * 6)},
                                         {'notation': 'b6', 'position': (self._field_y * 5, self._field_x * 6)},
                                         {'notation': 'b7', 'position': (self._field_y * 6, self._field_x * 6)},
                                         {'notation': 'b8', 'position': (self._field_y * 7, self._field_x * 6)},

                                         {'notation': 'c1', 'position': (self._field_y * 0, self._field_x * 5)},
                                         {'notation': 'c2', 'position': (self._field_y * 1, self._field_x * 5)},
                                         {'notation': 'c3', 'position': (self._field_y * 2, self._field_x * 5)},
                                         {'notation': 'c4', 'position': (self._field_y * 3, self._field_x * 5)},
                                         {'notation': 'c5', 'position': (self._field_y * 4, self._field_x * 5)},
                                         {'notation': 'c6', 'position': (self._field_y * 5, self._field_x * 5)},
                                         {'notation': 'c7', 'position': (self._field_y * 6, self._field_x * 5)},
                                         {'notation': 'c8', 'position': (self._field_y * 7, self._field_x * 5)},

                                         {'notation': 'd1', 'position': (self._field_y * 0, self._field_x * 4)},
                                         {'notation': 'd2', 'position': (self._field_y * 1, self._field_x * 4)},
                                         {'notation': 'd3', 'position': (self._field_y * 2, self._field_x * 4)},
                                         {'notation': 'd4', 'position': (self._field_y * 3, self._field_x * 4)},
                                         {'notation': 'd5', 'position': (self._field_y * 4, self._field_x * 4)},
                                         {'notation': 'd6', 'position': (self._field_y * 5, self._field_x * 4)},
                                         {'notation': 'd7', 'position': (self._field_y * 6, self._field_x * 4)},
                                         {'notation': 'd8', 'position': (self._field_y * 7, self._field_x * 4)},

                                         {'notation': 'e1', 'position': (self._field_y * 0, self._field_x * 3)},
                                         {'notation': 'e2', 'position': (self._field_y * 1, self._field_x * 3)},
                                         {'notation': 'e3', 'position': (self._field_y * 2, self._field_x * 3)},
                                         {'notation': 'e4', 'position': (self._field_y * 3, self._field_x * 3)},
                                         {'notation': 'e5', 'position': (self._field_y * 4, self._field_x * 3)},
                                         {'notation': 'e6', 'position': (self._field_y * 5, self._field_x * 3)},
                                         {'notation': 'e7', 'position': (self._field_y * 6, self._field_x * 3)},
                                         {'notation': 'e8', 'position': (self._field_y * 7, self._field_x * 3)},

                                         {'notation': 'f1', 'position': (self._field_y * 0, self._field_x * 2)},
                                         {'notation': 'f2', 'position': (self._field_y * 1, self._field_x * 2)},
                                         {'notation': 'f3', 'position': (self._field_y * 2, self._field_x * 2)},
                                         {'notation': 'f4', 'position': (self._field_y * 3, self._field_x * 2)},
                                         {'notation': 'f5', 'position': (self._field_y * 4, self._field_x * 2)},
                                         {'notation': 'f6', 'position': (self._field_y * 5, self._field_x * 2)},
                                         {'notation': 'f7', 'position': (self._field_y * 6, self._field_x * 2)},
                                         {'notation': 'f8', 'position': (self._field_y * 7, self._field_x * 2)},

                                         {'notation': 'g1', 'position': (self._field_y * 0, self._field_x * 1)},
                                         {'notation': 'g2', 'position': (self._field_y * 1, self._field_x * 1)},
                                         {'notation': 'g3', 'position': (self._field_y * 2, self._field_x * 1)},
                                         {'notation': 'g4', 'position': (self._field_y * 3, self._field_x * 1)},
                                         {'notation': 'g5', 'position': (self._field_y * 4, self._field_x * 1)},
                                         {'notation': 'g6', 'position': (self._field_y * 5, self._field_x * 1)},
                                         {'notation': 'g7', 'position': (self._field_y * 6, self._field_x * 1)},
                                         {'notation': 'g8', 'position': (self._field_y * 7, self._field_x * 1)},

                                         {'notation': 'h1', 'position': (self._field_y * 0, self._field_x * 0)},
                                         {'notation': 'h2', 'position': (self._field_y * 1, self._field_x * 0)},
                                         {'notation': 'h3', 'position': (self._field_y * 2, self._field_x * 0)},
                                         {'notation': 'h4', 'position': (self._field_y * 3, self._field_x * 0)},
                                         {'notation': 'h5', 'position': (self._field_y * 4, self._field_x * 0)},
                                         {'notation': 'h6', 'position': (self._field_y * 5, self._field_x * 0)},
                                         {'notation': 'h7', 'position': (self._field_y * 6, self._field_x * 0)},
                                         {'notation': 'h8', 'position': (self._field_y * 7, self._field_x * 0)}]

        self._field_x, self._field_y = _field_x, _field_y

    @property
    def _get_notation_white_on_the_bottom(self):
        """
        Return directory which contains dicrectories of pairs looking like this: notation + yx coordinates
        Example: {'notation': 'a2', 'position': (self._field_y * 1, self._field_x * 7)}

        :return self._white_pieces_on_the_bottom
        """
        return self._white_pieces_on_the_bottom

    @property
    def _get_notation_black_on_the_bottom(self):
        """
        Return directory which contains dicrectories of pairs looking like this: notation + yx coordinates
        Example: {'notation': 'a2', 'position': (self._field_y * 1, self._field_x * 7)}

        :return self._white_pieces_on_the_bottom
        """
        return self._black_pieces_on_the_bottom

    