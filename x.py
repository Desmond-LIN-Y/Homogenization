'''
Aim: prove that solution using finite differences, when using smaller lattice space, the solution converge to the result using homogenisation.
'''

import numpy as np
from random import choice
from copy import deepcopy
A_ep=np.array(
    [
        [1,2],
        [2,1]
    ]
)

A_ep2=np.array(
    [
        [1,2,1,2],
        [2,1,2,1],
        [1,2,1,2],
        [2,1,2,1],
    ]
)

def coefs(i,j):
    if (i+j)%2==0:
        #up,left,down,right
        return (1,2,2,1)
    else:
        return (2,1,1,2)
dim=55
grid=np.zeros((dim,dim))
#print(grid)
center=int((dim-1)/2)
grid[center,center]=320
def update(i,j):
    #gives updated value of i,j point
    up=grid[i-1,j]
    left=grid[i,j-1]
    down=grid[i+1,j]
    right=grid[i,j+1]
    co=coefs(i,j)
    '''
    b=(
        co[1]*co[2]*co[3]
    +co[0]*co[2]*co[3]
    +co[0]*co[1]*co[3]
    +co[0]*co[1]*co[2]
    )
    '''

    val=(
        up*co[1]*co[2]*co[3]
        +left*co[0]*co[2]*co[3]
        +down*co[0]*co[1]*co[3]
        +right*co[0]*co[1]*co[2]
    )/6

    return val
newgrid=deepcopy(grid)
for time in range(100):
    
    for i in range(1,dim-1):
        for j in range(1,dim-1):
            newgrid[i,j]=update(i,j)
    newgrid[center,center]=grid[center,center]
    
    grid=deepcopy(newgrid)
    print(time)
#print(grid)
def u(x,y):
    return newgrid[x,y]
from matplotlib import pyplot as plt
a=[i for i in range(dim)]
x,y=np.meshgrid(a,a)
plt.matshow(grid, cmap=plt.cm.gray)
plt.show()