import board
import player

class Game:

    """
    class representing a game state
    Attributes:
        board (list): A list of size 9 representing the game board
        player (int): the number indicating the current player, 1 for X, -1 for O
    """

    def __init__(self):
        """
        create a new game
        """
        self.board = board.Board()
        self.player = []
        self.player.append(player.Human(1, "Player 1"))
        self.player.append(player.Bot(2, "Player 2"))
        self.round = 0

    def ply(self):
        """
        make a ply
        Parameters:
        """
        self.board.print_board()
        num_player = self.round % 2

        while not self.board.is_won_quick(num_player+1):
            num_player = self.round % 2
            num_play = self.player[num_player].play(self.board)
            self.board.play(num_play, self.player[num_player].get_label())
            self.board.print_board()
            self.round += 1
        
        self.round -= 1
        p = self.player[self.round % 2]
        print("{} player as won : {} ({})".format(p.type, p.get_name(), board.pion[p.get_label()]))