import board
import statistics
import random

MaxDeep = 5
analyzed_board = {}
Max_eval = 100

class tree_node(object):
    def __init__(self, parent, cur_board, last_player, col_played, who_am_I = 2):
        self.parent = parent
        self.end_node = False
        self.ia_label = who_am_I
        self.last_player_label = last_player
        self.col_payed = col_played
        self.data = cur_board
        self.children = {}
        self.evaluation = None
        self.tested_won = False

    def update_evaluation(self,depth):
        # print(f"Debug Num play = {self.data.num_play} / depth = {depth} / last player =  {self.last_player_label} / last col =  {self.col_payed}")
        if self.end_node:
            # print ("Wn EndNod")
            return self.evaluation

        if not self.tested_won :
            # print ("testing won")
            self.tested_won = True
#            if self.data.is_won(self.last_player_label):
            if self.data.is_won_quick(self.last_player_label):
                # if self.data.is_won_quick(self.last_player_label):
                #     print ("check win ok")
                # else :
                #     print ("check win diffrent !!!")

                self.end_node = True
                if self.last_player_label == self.ia_label: #c'est le bot qui vient de jouer et a gagné
                    self.evaluation = Max_eval
                else : # c'est un humain qui vient de jouer et a gagné
                    self.evaluation = - Max_eval
        # else :
            # print("aleready tested")

        if self.end_node:
            # print ("Wn EndNod after test won")
            return self.evaluation


        if depth == 0: # on arrive au bout on met une évaluation neutre
            self.evaluation = 0
        else: # il faut évaluer les children
            list_eval = []
            for col in range(board.nbcol):
                child_player = nextPlayer(self.last_player_label)
                if self.data.can_play(col):
                    if col in self.children.keys():
                        self.children[col].update_evaluation(depth-1)
                    else: #create children
                        # print(f"create new child for {child_player} wit col {col}")
                        new_board = self.data.copy()
                        new_board.play(col, child_player)
                        new_hash = new_board.get_hash()
                        # new_board.print_board()
                        self.children[col] = tree_node(self, new_board, child_player, col_played=col, who_am_I=self.ia_label)
                        if not (new_hash in analyzed_board.keys()):
                            analyzed_board[new_hash] = self.children[col]
                        self.children[col].update_evaluation(depth-1)
                    list_eval.append(self.children[col].evaluation)
            # print("list eval    ", list_eval)
            self.evaluation = statistics.mean(list_eval)


    def bestmove(self):
        idx_move = []
        best_ev = -100
        for c in self.children:
            child = self.children[c]
            # print(f" child : {c} ev: {child.evaluation}")
            if child.evaluation > best_ev:
                idx_move = [child.col_payed]
                best_ev = child.evaluation
            elif child.evaluation == best_ev: 
                idx_move.append(child.col_payed)


        if len(idx_move) > 1:
            print ("play random in", idx_move)
            toplay = idx_move[random.randint(0,len(idx_move)-1)]
        else : 
            toplay = idx_move[0]

        print(" play ", toplay)
        return toplay


def bestmove(cur_board):
    curr_hash = cur_board.get_hash()
#    print(f" debug hash found = {curr_hash}")
    if not (curr_hash in analyzed_board.keys()):
        # print("curr Hash no found")
        analyzed_board[curr_hash] = tree_node(None,board.Board(), 0, 0)
    # else :
    #     print(" Corresponding Board")
    #     analyzed_board[curr_hash].data.print_board()
    #     print(" ___________________")
    
    analyzed_board[curr_hash].update_evaluation(MaxDeep)
    curr_best_move = analyzed_board[curr_hash].bestmove()
    return curr_best_move

def nextPlayer(label):
    if label == 1:
        return 2
    else:
        return 1