# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:46:34 2020

@author: Séverine Ehrhardt (11724920)
"""
import numpy as np
import matplotlib.pyplot as plt

def local_temp(A, albedo, T, q=30):
    """Calculate local temperature experienced by a particular daisy type or 
    ground cover. This is a simplified version of the original.
    q*(A-albedo)+T
    
    Arguments
    ---------
    A : float
        Planetary albedo
    alpha : float
        Albedo of daisy type
    T : float
        Planetary temperature.
    
    Keyword Arguments
    -----------------
    q = 30 : float
        Heat transfer coefficient
    """
    return q*(A-albedo)+T


def planetary_temp(S, A, L=1.0):
    """Calculate the planetary temperature.
    SL(1-A) = sT**4
    
    Arguments
    ---------
    S : float
        Incident solar energy.
    A : float
        Planetary albedo.

    Keyword Arguments
    -----------------
    L = 1.0 : float
        Normalised stellar luminosity.
    """
    sigma = 5.67032e-8 # Stephan-Bolzmann constant.
    return ((S*L*(1-A))/sigma)**(1/4.)