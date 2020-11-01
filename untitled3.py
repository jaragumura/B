#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:07:18 2020

@author: fistlab

"""
import numpy as np

def morphological(im, operator=np.min, nx=5, ny=5):
    newIm = np.zeros(im.shape)
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            nlst = neighbours(im, x, y, nx, ny)
            newIm[x,y] = operator(nlst)
    return newIm

def neighbours(im, x, y, nx=1, ny=1):
    return im[max(x-nx, 0) : min(x+nx+1, im.shape[0]), \
                      max(y-ny, 0) : min(y+ny+1, im.shape[1])]
        
def erosion(im, nx=5, ny=5):
    return morphological(im, np.min, nx, ny)

def dilation(im, nx=5, ny=5):
     return morphological(im, np.max, nx, ny)