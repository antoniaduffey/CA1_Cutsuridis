# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:57:40 2020

@author: mbezaire
"""
import subprocess

def get_sys_args(argvlist,varnames):
    
    dict2define = {}
    varvals = []
    # Check for parameters being passed in via the command line
    argadd = 1
    startlen = 1
    result = subprocess.run('hostname', stdout = subprocess.PIPE)
    if (result.stdout.decode('utf-8')[:3] == "scc"): # scc has an odd way of accounting for command line arguments
        argadd = 2
        startlen = 5
        
    if len(argvlist)>(startlen):
        varvals.append(argvlist[startlen])
        if len(argvlist)>(argadd+startlen):
            varvals.append(float(argvlist[argadd+startlen]))
            if len(argvlist)>(2*argadd+startlen):
                varvals.append(float(argvlist[2*argadd+startlen]))
                if len(argvlist)>(3*argadd+startlen):
                    varvals.append(int(argvlist[3*argadd+startlen]))
                    if len(argvlist)>(4*argadd+startlen):
                        varvals.append(float(argvlist[4*argadd+startlen]))

    for key, val in zip(varnames, varvals):
        dict2define[key] = val
    
    return dict2define
