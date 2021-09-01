# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 23:32:33 2021

@author: DELL
"""

import math
import numpy as np


def exacta():
    r0 = 1/2
    a = 1
    t = 1
    R = 1
    return (r0)/(r0+math.e**(-a*t)*(R-r0))

def ynLog(N):
    y0 = 1/2
    dt = 1/N
    R = 1
    a = 1
    y_ = np.array([y0 for _ in range(N+1)])
    for i in range(N):
        y_[i+1] = a*y_[i]*(1-(y_[i]/R))*dt+y_[i]
    return y_[N]

def znLog(N):
    z0 = 1/2
    dt = 1/N
    z_ = np.array([z0 for _ in range(N+1)])
    for i in range(N):
        z_[i+1] = ((-1*(1-dt)+math.sqrt(((1-dt)**2-4*(dt)*(-z_[i]))))/(2*dt))
    return z_[N]

def errorAbsExplicito(num):
    return abs(exacta()-ynLog(num))

def errorAbsImplicito(num):
    return abs(exacta()-znLog(num))
    


N = 1
print("-----------------------")
for i in range(100):
    if(i==0):
        print()
    else:
        N += 10        
    print("Explícito: ", ynLog(N))
    print("Error Abs Ex: ", errorAbsExplicito(N))
    print("Implicita:  ", znLog(N)) 
    print("Error Abs Im: ", errorAbsImplicito(N))
    print("Exacta: ", exacta())    
    print("Valor de N: ", N)
    print("")
    print("-----------------------")
    
