nbcol = 7
nbligne = 6

grille = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,1,2,0,0,0]
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

