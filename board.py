import numpy as np
import hashlib

nbcol = 7
nbligne = 6

pion = [' ', 'X', 'O']

def print_top_line():
    print(u'\u250c', end = '')
    for _ in range(nbcol-1):
        print(u'\u2500\u252c', sep = '', end = '')
    print(u'\u2500\u2510')

def print_mid_line_empty(tab_line):
    for i in range(nbcol):
        print(u'\u2502',pion[tab_line[i]], sep = '', end = '')
    print(u'\u2502')

def print_mid_line_full():
    print(u'\u251c', end = '')
    for _ in range(nbcol-1):
        print(u'\u2500\u253c', end = '')
    print(u'\u2500\u2524')

def print_bottom_line():
    print(u'\u2514', end = '')
    for _ in range(nbcol-1):
        print(u'\u2500\u2534', end = '')
    print(u'\u2500\u2518')

def print_numbers():
    print(" ", end = '')
    for i in range(nbcol):
        print(i, end = '')
        print(' ', end = '')
    print()

def get_diagonal_gauche(g):
    tab=[]
    for d in range(6):
        i = min(d+3,nbcol-1)
        j = max(0,d-3)
        l=[]
        while i>=0 and j<=nbligne-1 :
            l.append(g[j,i])
            i-=1
            j+=1
        tab.append(l)
    return tab

def get_diagonal_droite(g):
    tab=[]
    for d in range(7):
        i = max(0,d-2)
        j = max(2-d,0)
        l=[]
        while i<nbcol and j<nbligne :
            #print ('i=',i,'j=',j, 'x=',g[j,i] )
            l.append(g[j,i])
            i+=1
            j+=1
        tab.append(l)
    return tab

def get_horizontal(g):
    return g

def get_vertical(g):
    return g.T

def test_4_successif (ligne,joueur):
    for i in range (len(ligne)-3):
        if (ligne[i] == joueur and ligne[i+1] == joueur and ligne[i+2] == joueur and ligne[i+3] == joueur):
           return True
    return False


class Board(object):
    def __init__(self, grille = None):
        if grille is None:
            self.grille = np.array([
                                    [0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0],
                                    [0,0,0,0,0,0,0],
                                ])
        else:
            self.grille = grille.copy()
        self.num_play = 0
        self.moves = []
        self.height = [0, 7, 14, 21, 28, 35, 42]
        self.bitboard = [0]*2


    def print_board(self):
        print_top_line()
        for i in range(nbligne-1):
            print_mid_line_empty(self.grille[i])
            print_mid_line_full()
        print_mid_line_empty(self.grille[nbligne-1])
        print_bottom_line()
        print_numbers()

    def play(self,col, label):
        play_row_in_col = nbligne - 1 - np.count_nonzero(self.grille.T[col])
        self.grille[play_row_in_col,col] = label
        self.num_play +=1

        self.height[col] += 1
        move = 1 << self.height[col]
        self.bitboard[self.num_play & 1] ^= move
        self.moves.append(col)


    def copy(self):
        new_board = Board()
        new_board.grille = self.grille.copy()
        new_board.num_play = self.num_play
        new_board.bitboard = self.bitboard.copy()
        new_board.moves = self.moves.copy()
        new_board.height = self.height.copy()
        return new_board

    def can_play(self, move):
        return self.grille[0,move] == 0

    def get_hash(self):
        return hashlib.sha256(self.grille.tobytes()).hexdigest()

    def is_won(self,player):
        for l in get_horizontal(self.grille):
            if test_4_successif(l,player):
                return player
        for l in get_vertical(self.grille):
            if test_4_successif(l,player):
                return player
        for l in get_diagonal_gauche(self.grille):
            if test_4_successif(l,player):
                return player
        for l in get_diagonal_droite(self.grille):
            if test_4_successif(l,player):
                return player
        return 0

    def is_won_quick(self, player):
        directions = [1, 6, 7, 8]
        bb_player = self.bitboard[player & 1]
        bb = 0
        for d in directions:
            bb = bb_player & (bb_player >> d)
            if ((bb & (bb >> (2* d))) != 0):
                return True
        return False
# boolean isWin(long bitboard) {
#     int[] directions = {1, 7, 6, 8};
#     long bb;
#     for(int direction : directions) {
#         bb = bitboard & (bitboard >> direction);
#         if ((bb & (bb >> (2 * direction))) != 0) return true;
#     }
#     return false;
# }
