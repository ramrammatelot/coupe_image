# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:43:28 2023

@author: ram
"""
import skimage 
contenu = skimage.io.imread('nb.png')
matrice= list(list(i) for i in contenu)