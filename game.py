# chess game

WHITE = "W"
BLACK = "B"

class Piece:
    def __init__(self, init_x, init_y, color):
        self.position = [init_x, init_y]
        self.color = color
        self.alive = True
        self.name = None
        
    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def get_legal_moves(self, board):
        pass

    # this has to be overriden for all pieces except knight and king
    def is_legal_move(self, board, move):
        x, y = move[:]

        if (0 > x or x > 7) or (0 > y or y > 7):
            return False

        if board.is_empty_at_position(move):
            return True

        return board.color_at_position(move) != self.color

        
class Pawn(Piece):
    def __init__(self, init_x, init_y, color):
        super().__init__(init_x, init_y, color)
        self.name = "Pawn"
        
    # TODO: En passant move check... will this require board state history?... maybe just the last move by opp
    def get_legal_moves(self, board):
        x, y = self.position[:]
        dx = 1 if self.color == WHITE else -1
        dy = 1
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
    def __init__(self, init_x, init_y, color):
        super().__init__(init_x, init_y, color)
        self.name = "Rook"
        self.can_castle = True
        
    # need to add castling check
    def get_legal_moves(self, board):
        x, y = self.position[:]
        y_pos_moves = [[x, y + i] for i in range(1, 8)]
        y_neg_moves = [[x, y - i] for i in range(1, 8)]
        x_pos_moves = [[x + i, y] for i in range(1, 8)]
        x_neg_moves = [[x - i, y] for i in range(1, 8)]
        possible_moves = [y_pos_moves, y_neg_moves, x_pos_moves, x_neg_moves]
        legal_moves = []
        for moves in possible_moves:
            for move in moves:
                mx, my = move[:]
                if (0 <= mx <= 7) and (0 <= my <= 7):
                    if board.is_empty_at_position(move):
                        legal_moves.append(move)
                    else:
                        if board.color_at_position(move) != self.color:
                            legal_moves.append(move)
                            break
                        else:
                            break
        return legal_moves
        

class Knight(Piece):
    def __init__(self, init_x, init_y, color):
        super().__init__(init_x, init_y, color)
        self.name = "Knight"
        
    def get_legal_moves(self, board):
        x, y = self.position[:]
        possible_moves = [[x + 2, y + 1], [x + 2, y - 1], [x - 2, y + 1], [x - 2, y - 1],
                          [x + 1, y + 2], [x + 1, y - 2], [x - 1, y + 2], [x - 1, y - 2]]
        legal_moves = []
        for move in possible_moves:
            if self.is_legal_move(board, move):
                legal_moves.append(move)
        return legal_moves

class Bishop(Piece):
    def __init__(self, init_x, init_y, color):
        super().__init__(init_x, init_y, color)
        self.name = "Bishop"
        
    def get_legal_moves(self, board):
        x, y = self.position[:]
        diag_up_right = [[x + i, y + i] for i in range(1, 8)]
        diag_up_left = [[x + i, y - i] for i in range(1, 8)]
        diag_down_right = [[x - i, y + i] for i in range(1, 8)]
        diag_down_left = [[x - i, y - i] for i in range(1, 8)]
        possible_moves = [diag_up_right, diag_up_left, diag_down_left, diag_down_right]
        legal_moves = []
        for moves in possible_moves:
            for move in moves:
                mx, my = move[:]
                if (0 <= mx <= 7) and (0 <= my <= 7):
                    if board.is_empty_at_position(move):
                        legal_moves.append(move)
                    else:
                        if board.color_at_position(move) != self.color:
                            legal_moves.append(move)
                            break
                        else:
                            break
        return legal_moves

class King(Piece):
    def __init__(self, init_x, init_y, color):
        super().__init__(init_x, init_y, color)
        self.can_castle = True
        self.name = "King"

    def get_legal_moves(self, board):
        x, y = self.position[:]
        legal_moves = []
        moves = [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y], [x + 1, y + 1], [x + 1, y - 1], [x - 1, y + 1], [x - 1, y - 1]]
        for move in moves:
            if self.is_legal_move(board, move):
                legal_moves.append(move)
        return legal_moves

class Queen(Piece):
    def __init__(self, init_x, init_y, color):
        super().__init__(init_x, init_y, color)
        self.name = "Queen"
        
    def get_legal_moves(self, board):
        x, y = self.position[:]
        diag_up_right = [[x + i, y + i] for i in range(1, 8)]
        diag_up_left = [[x + i, y - i] for i in range(1, 8)]
        diag_down_right = [[x - i, y + i] for i in range(1, 8)]
        diag_down_left = [[x - i, y - i] for i in range(1, 8)]
        y_pos_moves = [[x, y + i] for i in range(1, 8)]
        y_neg_moves = [[x, y - i] for i in range(1, 8)]
        x_pos_moves = [[x + i, y] for i in range(1, 8)]
        x_neg_moves = [[x - i, y] for i in range(1, 8)]
        possible_moves = [diag_up_right, diag_up_left, diag_down_left, diag_down_right, y_pos_moves, y_neg_moves, x_pos_moves, x_neg_moves]
        legal_moves = []
        for moves in possible_moves:
            for move in moves:
                mx, my = move[:]
                if (0 <= mx <= 7) and (0 <= my <= 7):
                    if board.is_empty_at_position(move):
                        legal_moves.append(move)
                    else:
                        if board.color_at_position(move) != self.color:
                            legal_moves.append(move)
                            break
                        else:
                            break
        return legal_moves

class Board:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_color_turn = WHITE

    def initialize_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]

        board[0][0] = Rook(0, 0, BLACK)
        board[0][1] = Knight(0, 1, BLACK)
        board[0][2] = Bishop(0, 2, BLACK)
        board[0][3] = Queen(0, 3, BLACK)
        board[0][4] = King(0, 4, BLACK)
        board[0][5] = Bishop(0, 5, BLACK)
        board[0][6] = Knight(0, 6, BLACK)
        board[0][7] = Rook(0, 7, BLACK)
        board[1][0] = Pawn(1, 0, BLACK)
        board[1][1] = Pawn(1, 1, BLACK)
        board[1][2] = Pawn(1, 2, BLACK)
        board[1][3] = Pawn(1, 3, BLACK)
        board[1][4] = Pawn(1, 4, BLACK)
        board[1][5] = Pawn(1, 5, BLACK)
        board[1][6] = Pawn(1, 6, BLACK)
        board[1][7] = Pawn(1, 7, BLACK)
        
        board[7][0] = Rook(7, 0, WHITE)
        board[7][1] = Knight(7, 1, WHITE)
        board[7][2] = Bishop(7, 2, WHITE)
        board[7][3] = Queen(7, 3, WHITE)
        board[7][4] = King(7, 4, WHITE)
        board[7][5] = Bishop(7, 5, WHITE)
        board[7][6] = Knight(7, 6, WHITE)
        board[7][7] = Rook(7, 7, WHITE)
        board[6][0] = Pawn(6, 0, WHITE)
        board[6][1] = Pawn(6, 1, WHITE)
        board[6][2] = Pawn(6, 2, WHITE)
        board[6][3] = Pawn(6, 3, WHITE)
        board[6][4] = Pawn(6, 4, WHITE)
        board[6][5] = Pawn(6, 5, WHITE)
        board[6][6] = Pawn(6, 6, WHITE)
        board[6][7] = Pawn(6, 7, WHITE)

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

    def update_board_state(self, position, move):
        pass
    
    def is_empty_at_position(self, position):
        x, y = position[:]
        if self.board[x][y]:
            return False
        return True

    def color_at_position(self, position):
        x, y = position[:]
        return self.board[x][y].get_color()
    

if __name__ == '__main__':

    # main game loop here
    i = 0
    game_over = False
    board = Board()
