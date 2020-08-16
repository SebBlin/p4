import numpy as np

grille = np.array([
    [0,0,0,0,0,0,0],
    [0,0,1,0,5,0,0],
    [0,0,1,1,0,0,0],
    [0,0,1,0,0,0,0],
    [0,1,2,0,0,1,0],
    [1,1,2,2,2,1,1],
])

for k in range(-2,4):
    print(np.diag(grille, k=k))

print('t')
for k in range(-3,4):
    print(np.diag(grille.T, k=k))