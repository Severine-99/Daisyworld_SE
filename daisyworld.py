#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Séverine Ehrhardt (11724920)
"""

import numpy as np
import matplotlib.pyplot as plt

from albedo import*
from replicator import*
from beta import*
from euler import*
from temperature import*
from variables import*

if __name__ == '__main__':
    # Main loop for changing luminosity
    for i,L in enumerate(luminosities):
        # Set a minimum for cover fractions
        if alphaw<0.01: alphaw = 0.01
        if alphab<0.01: alphab = 0.01
        alphag = p-alphaw-alphab
        # Reset counters
        n = 0
        changew, changeb = 1,1
        # Run loop for daisy earth.
        while (n<maxn) and (changew>tol) and (changeb>tol):
            # Store the initial cover fractions
            sw,sb = alphaw, alphab
            # Planetary albedo
            planet_albedo = albedo(alphaw,alphab,alphag,aw,ab,ag)
            # Planetary temperature
            T = planetary_temp(S,planet_albedo, L=L)
            # Local temperature
            Tw = local_temp(planet_albedo,aw,T)
            Tb = local_temp(planet_albedo,ab,T)
            # Birth rate
            betaw = beta(Tw)
            betab = beta(Tb)
            # Change in daisies
            dawdt = daisy_replicator(alphaw, alphag, betaw, gamma)
            dabdt = daisy_replicator(alphab, alphag, betab, gamma)
            # Integrate
            alphaw = euler(alphaw, dawdt)
            alphab = euler(alphab, dabdt)
            alphag = p-alphaw-alphab
            n += 1
        # Store the output
        alphaw_out[i] = alphaw
        alphab_out[i] = alphab
        temp_out[i] = T

# Plot the results
# Cover fractions
white = plt.plot(luminosities,alphaw_out*100,'b', label='White')
black = plt.plot(luminosities,alphab_out*100,'k', label='Black')
plt.legend(loc='upper right')
plt.xlabel('Luminosity')
plt.ylabel('Surface cover %')
plt.title('Cover fractions')
plt.show()

# Planetary temperature
plt.figure()
plt.plot(luminosities,temp_out-273.15,'r')
plt.xlabel('Luminosity')
plt.ylabel('Temperature (°C)')
plt.title('Planetary temperature')
plt.show()
