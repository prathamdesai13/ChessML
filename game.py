# chess game

WHITE = "W"
BLACK = "B"

class Piece:
    def __init__(self, name, init_x, init_y, color):
        self.name = name
        self.position = [init_x, init_y]
        self.color = color
        self.alive = True

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def get_legal_moves(self, board):
        pass


class Pawn(Piece):
    def __init__(self, name, init_x, init_y, color):
        super().__init__(name, init_x, init_y, color)

    def get_legal_moves(self, board):
        # pawn moveset x -> x, x + 1, x - 1 | y -> y + 1
        x, y = self.position[:]
        dx = 1 if self.color == WHITE else -1
        dy = 1
        possible_moves = [[x + dx, y], [x + dx, y + dy], [x + dx, y - dy]]
        legal_moves = []
        if (0 <= x + dx <= 7) and (0 <= y <= 7) and board.is_empty_at_position([x + dx, y]):
            legal_moves.append([x + dx, y])

        if (0 <= x + dx <= 7) and (0 <= y + dy <= 7) and (not board.is_empty_at_position([x + dx, y + dy])):
            if board.color_at_position([x + dx, y + dy]) != self.color:
                legal_moves.append([x + dx, y + dy])

        if (0 <= x + dx <= 7) and (0 <= y - dy <= 7) and (not board.is_empty_at_position([x + dx, y - dy])):
            if board.color_at_position([x + dx, y - dy]) != self.color:
                legal_moves.append([x + dx, y - dy])
        return legal_moves
        
class Rook(Piece):
    def __init__(self, name, init_x, init_y, color):
        super().__init__(name, init_x, init_y, color)        

class Knight(Piece):
    def __init__(self, name, init_x, init_y, color):
        super().__init__(name, init_x, init_y, color)

class Bishop(Piece):
    def __init__(self, name, init_x, init_y, color):
        super().__init__(name, init_x, init_y, color)

class King(Piece):
    def __init__(self, name, init_x, init_y, color):
        super().__init__(name, init_x, init_y, color)

class Queen(Piece):
    def __init__(self, name, init_x, init_y, color):
        super().__init__(name, init_x, init_y, color)

class Board:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_color_turn = WHITE

    def initialize_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        board[0][4] = Pawn("Pawn", 0, 4, BLACK)
        board[0][5] = Pawn("Pawn", 0, 5, BLACK)
        board[0][6] = Pawn("Pawn", 0, 6, BLACK)
        board[1][5] = Pawn("Pawn", 1, 5, WHITE)
        board[1][4] = Pawn("Pawn", 1, 4, BLACK)
        board[1][6] = Pawn("Pawn", 1, 6, BLACK)
        board[2][4] = Pawn("Pawn", 2, 4, BLACK)
        board[2][5] = Pawn("Pawn", 2, 5, BLACK)
        board[2][6] = Pawn("Pawn", 2, 6, BLACK)
        return board

    def print_board(self):
        for row in range(8):
            for col in range(8):
                if self.board[row][col]:
                    color = self.board[row][col].get_color()
                    piece = self.board[row][col].get_name()
                    print(f"{color}{piece}", end=" ")
                else:
                    print(None, end=" ")
            print("\n")

    def update_board_state(self, move):
        pass

    def is_empty_at_position(self, position):
        x, y = position[:]
        if self.board[x][y]:
            return False
        return True

    def color_at_position(self, position):
        x, y = position[:]
        return self.board[x][y].get_color()
    
def initialize_board(board):
    pass


if __name__ == '__main__':

    # main game loop here
    i = 0
    game_over = False
    board = Board()
    board.print_board()
    pawn = board.board[1][5]
    print(pawn.get_legal_moves(board))
