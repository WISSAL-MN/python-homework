# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from search import *


theProblem = GraphProblem('Arad','Pitesti',romania_map)
result1 = breadth_first_tree_search(theProblem)
print(result1.path())
result2 = best_first_graph_search(theProblem, theProblem.h)
print(result2.path())
