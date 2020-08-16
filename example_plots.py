# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:37:49 2020

@author: mbezaire
"""

import matplotlib.pyplot as plt

simname = "sim1"
SIMDUR = 2050
dt = 0.025
numCycles = 8
network_scale = 1
netfile = 'N100S20P5'

spks = np.loadtxt("{}_spt.dat".format(netfile),skiprows=1)
plt.figure()
plt.scatter(spks[:,0],spks[:,1],s=.1)
plt.xlabel("Time (ms)")
plt.ylabel("Neuron #")
plt.title("Spike Raster")
plt.show()

pvsoma = np.loadtxt("{}_pvsoma.dat".format(netfile),skiprows=1)
plt.figure()
plt.plot(pvsoma[:,0],pvsoma[:,1])
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.title("Pattern Pyramidal Cell")
plt.show()

import fig9_patternrecall as fig9
import fig10_Vtraces as fig10

fig9.plot_results(simname,netfile,numCycles, network_scale)
fig10.plot_voltages(simname, 200, SIMDUR,dt)

