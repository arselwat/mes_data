# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:48:14 2022

@author: ASUS
"""
from math import *
from abc import ABCMeta, abstractmethod 

class forme_geometrique(metaclass=ABCMeta):
    
    @abstractmethod
    
    def surface(self):
        return  
    def perimetre(self):
        return     
class rectangle(forme_geometrique):
    def __init__(self,hauteur,larg):
        self.hauteur=hauteur
        self.larg=larg
        def surface(self):
            return self.hauteur*self.larg
    
        def perimetre(self):
            return (self.hauteur+self.larg)*2
class cercle(forme_geometrique):
    def __init__(self, rayon):
        self.rayon=rayon
        def surface(self):
            return pi*rayon**2
        def perimetre(self):
            return 2*pi*self.rayon
        
class triangle(forme_geometrique):
    def __init__(self,haut,base):
        self.haut=haut
        self.base=base
        def surface(self):
            return self.haut*self.base/2
    
    
tr=triangle().surface(5,8)   
    
    
    