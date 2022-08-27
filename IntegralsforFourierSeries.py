# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 10:17:47 2022

@author: Nicholas
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

#importing the integrate function
from scipy.integrate import quad

#Inputting Desired Graph, over a period
#[here for square wave centred about y axis, with height of 1, and T=2L ]
f_1 = lambda x: 1
f_2 = lambda x: 0
#[assign L an arbitrary value]
L=1
bnd_1 = -L
bnd_2 = -L/2
bnd_3 = L/2
bnd_4 = L

T = 2*L
w = np.pi/L

#the 1st term calculation
a_teg1, ateg1_err = quad(f_2, bnd_1, bnd_2)
print(a_teg1)
a_teg2, ateg2_err= quad(f_1, bnd_2, bnd_3)
print(a_teg2)
a_teg3, ateg3_err = quad(f_2, bnd_3, bnd_4)
print(a_teg3)
a = (w/np.pi)*(a_teg1 + a_teg2 + a_teg3)
print(a)

