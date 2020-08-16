# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:40:26 2020

@author: mbezaire
"""
fstem="par"
with open("pyresults/{}_ncw.dat".format(fstem), 'w') as f:
    for nc in nclist:
        f.write("{:.6f}\n".format(nc.weight[0]))
        
with open("pyresults/{}_nce.dat".format(fstem), 'w') as f:
    for nc in ncelist:
        f.write("{:.6f}\n".format(nc.weight[0]))
        
with open("pyresults/{}_ncs.dat".format(fstem), 'w') as f:
    for nc in ncslist:
        f.write("{:.6f}\n".format(nc.weight[0]))
        
                

#%%
import numpy as np

pync = np.loadtxt(r'pyresults/par_ncs.dat')
hocnc = np.loadtxt(r'C:\Users\mbezaire\Desktop\123815-master\Results\HAM_P5R1_ncs.dat')



#%%
# o : 1720 pync weights are 0 instead of ...
CA3 to inrn and EC to inrn are 0

# 1720 - 1780 weights are ok: first sep -> bask, sep -> aac
1790 - 1830: second sep -> bask, sep -> aac not ok
# 1830 - 1930 weights are ok

1930 - 2930- pyr-> pyr, pyr -> bask, pyr -> bis, pyr -> aa, pyr -> olm not ok

# 2930 - 3834: Bas -> Pyr, Bas -> Bas, Bas -> Bis, AA -> Pyr, Bis -> Pyr(GABA)

3834 -4434 .0004 bis -> pyr not ok

# 4434 - 4636: Bis -> Bask and OLM -> Pyr (regular GABA)

4636+ 9 to 10 .0004 not ok

