#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:01:11 2017

@author: anaid
"""

#grafo = {(1, 3): 4, (2, 3): 2, (3, 4): 2, (2, 4): 1, (4, 6): 1, (5, 6): 2}
 
import Grafo
from copy import deepcopy

grafo=Grafo()
grafo.cargarGrafoRandom(5, 4, 20)

cand = deepcopy(grafo)
arbol = set()
peso = 0
comp = {}
 
while len(cand) > 0:
    arista = grafo.minPeso()
    (u, v) = arista.pop(0)  # se consideran una sola vez
    c = comp.get(v, {v})
    if u not in c:
        arbol.add(arista)
        peso += grafo[arista]
        nuevo = c.union(comp.get(u, {u}))
        for w in nuevo:
            comp[w] = nuevo  
    #        print comp
    #print '--------------------------------------'
 
 
 
print('MST con peso', peso, ':', arbol)