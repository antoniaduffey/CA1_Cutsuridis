# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:27:50 2021

@author: parsh
"""
class modelcell():
    def __init__(self):
        self.x = 0; self.y = 0; self.z = 0

        self.gid = -1
        self.core_i=-1
        self.coretype_i=-1
        
        self.is_art = 0
        self.nc = []
        self.pre_list = []
