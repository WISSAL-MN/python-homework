from search import *

prob = GraphProblem ( 'Arad' , 'Pitesti' , romania_map)
result=  breadth_first_tree_search (prob)
print (result.path())
resultt=  best_first_graph_search (prob,prob.h)
print (resultt.path())
 
  
#cd por acceder au do
#python nom du fichier