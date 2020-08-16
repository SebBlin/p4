import board
import random
import ai


class Bot(object):
    def __init__(self, label, name):
        self.type = "B"
        self.label = label
        self.name = name

    def get_name(self):
        return self.name

    def get_label(self):
        return self.label
    
    def play(self,cur_board):
        print('Bot playing')
        myplay = ai.bestmove(cur_board)
        return myplay

class Human(object):
    def __init__(self, label, name):
        self.type = "H"
        self.label = label
        self.name = name
    
    def get_name(self):
        return self.name

    def get_label(self):
        return self.label

    def play(self, cur_board):
        myplay = int(input("{} ({}), please take you action:".format(self.name,board.pion[self.label])))
        while(not cur_board.can_play(myplay)):
            print(' !! illegal move')
            myplay = int(input("{}, please take you action:".format(self.name)))
        return myplay