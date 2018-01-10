from qutip import *
from pylab import *
import numpy as np

def draw_ground():
    a = [0,0,-1]
    draw_bloch(a)

def draw_superposition():
    a = [0,1,0]
    draw_bloch(a)

def ground_state():
    psi = basis(2,1)
    return psi

def x_rotation(angle):
    return qutip.gates.rx(angle)

def show_sphere(psi):
    sphere = Bloch()
    sphere.zlabel=[r'|1>',r'|0>']
    sphere.add_states(psi)
    sphere.show()

def draw_bloch(vector):
    sphere=Bloch()
    #sphere.zlabel=[r'$|0\rangle$',r'$|1\rangle$']
    sphere.zlabel=[r'|1>',r'|0>']
    sphere.vector_color = ['r']
    sphere.add_vectors(vector)
    sphere.show()
