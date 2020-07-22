# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:45:38 2020

@author: Séverine Ehrhardt (11724920)
"""
import numpy as np
import matplotlib.pyplot as plt

def euler(initial, tendency, h=1):
    """Integrate forward in time using Euler's method of numerical integration.
    initial + h*tendency
    
    Arguments
    ---------
    initial :  float
        The initial state.
    tendency : float
        The rate of change in the initial state.
    
    Keyword arguments
    -----------------
    h = 1 : float
        The timestep duration.
    """
    return initial + h*tendency