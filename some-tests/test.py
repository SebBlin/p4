# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:42:28 2020

@author: marie
"""

nbcol = 7
nbligne = 6

import numpy as np

#print(grille)
#print(grille.T)

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
    """tot
    """
    for i in range (len(ligne)-3):
        if (np.count_nonzero(np.array(ligne[i:i+4]) == joueur,axis=0) == 4):
           return True
    return False

# n = np.array([1,1,1,1])
# print(np.count_nonzero(n == 1))

grille = np.array([
    [0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,1,0,0,0,0],
    [0,1,2,0,0,1,0],
    [1,1,2,2,2,1,1],
])

joueur = 1
print(np.any([test_4_successif(l,joueur) for l in get_horizontal(grille)]))
print(np.any([test_4_successif(l,joueur) for l in get_vertical(grille)]))
print(np.any([test_4_successif(l,joueur) for l in get_diagonal_gauche(grille)]))
print(np.any([test_4_successif(l,joueur) for l in get_diagonal_droite(grille)]))

exit(0)

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

print_top_line()
for i in range(nbligne-1):
    print_mid_line_empty(grille[i])
    print_mid_line_full()
print_mid_line_empty(grille[nbligne-1])
print_bottom_line()





# res=test_4_successif([2,2,2,2,2,1,1],2)
# print(res)
