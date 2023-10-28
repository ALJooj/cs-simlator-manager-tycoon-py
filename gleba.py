from tester import (
    Board, Pawn, Rook, King, Knight, Bishop, Queen,
    WHITE, BLACK
)

board = Board()
board.field = [([None] * 8) for i in range(8)]
board.field[0][3] = Queen(WHITE)
board.field[2][3] = Bishop(WHITE)
board.field[0][5] = Rook(WHITE)
queen = board.get_piece(0, 3)

for row in range(7, -1, -1):
    for col in range(8):
        if queen.can_move(board, 0, 3, row, col):
            print('x', end='')
        else:
            cell = board.cell(row, col)[1]
            cell = cell if cell != ' ' else '-'
            print(cell, end='')
    print()