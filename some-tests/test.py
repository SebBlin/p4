# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:42:28 2020

@author: marie
"""

nbcol = 7
nbligne = 6
ligne_1=[0,0,0,0,0,0,0]
ligne_2=[0,0,0,0,0,0,0]
ligne_3=[0,0,0,0,0,0,0]
ligne_4=[0,0,0,0,0,0,0]
ligne_5=[0,0,1,0,0,0,0]
ligne_6=[1,1,2,2,2,1,1]
grille = [
    ligne_1,
    ligne_2,
    ligne_3,
    ligne_4,
    ligne_5,
    ligne_6
]

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





# def condition_victoire(ligne):
#     compteur = 1
#     nombre_de_croix = ligne.count(1)
#     nombre_de_rond = ligne.count(2)
#     longueur_tableau = len(ligne)
#     print(longueur_tableau)
#     if nombre_de_croix >= 4:
#         for i in range (0,longueur_tableau-1):
#             if compteur >= 4 :
#                     print ("le joueur 1 a gagné")
#                     break
#             if (ligne[i]==1 & ligne[i+1]!=1):
#                 compteur=1
#             if (ligne[i]== 1 & ligne[i+1]==1):
#                 compteur=compteur+1
#     if nombre_de_rond >= 4:
#         for i in range (0,longueur_tableau-1):
#             if compteur >= 4 :
#                     print ("le joueur 2 a gagné")
#                     break
#             if (ligne[i]==2 & ligne[i+1]!=2):
#                 compteur=1
#             if (ligne[i]== 2 & ligne[i+1]==2):
#                 compteur=compteur+1
                
                
    
#     return (nombre_de_croix,nombre_de_rond,compteur,"toto")


# variable = [0,1,1,1,1,1,2]
# variable_2 = "oui"
# nbc,nbr,*r = condition_victoire ( [1,1,2,2,2,1,1])

# print ("le nombre de croix est de")
# print (nbc)
# print("le nombre de rond est de " )
# print(nbr)
# #print("le compteur est de" )
# #print(c)
# print (r)


def test_4_successif (ligne,joueur):
    """tot
    """
    for i in range (len(ligne)-3):
         if (ligne[i:i+4].count(joueur) == 4):
            return True
    return False
        

res=test_4_successif([2,2,2,2,2,1,1],2)
print (res)
