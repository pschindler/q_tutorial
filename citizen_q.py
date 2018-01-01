from qutip import *
import numpy as np

def draw_vectors():
    a = [0,0,-1]
    draw_bloch(a)
    b = [0,1,0] #/np.sqrt(2),1/np.sqrt(2)]
    draw_bloch(b)

def draw_bloch(vector):
    sphere=Bloch()
    #sphere.zlabel=[r'$|0\rangle$',r'$|1\rangle$']
    sphere.zlabel=[r'|1>',r'|0>']
    sphere.vector_color = ['r']
    sphere.add_vectors(vector)
    sphere.show()
