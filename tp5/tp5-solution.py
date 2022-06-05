# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:48:25 2021

@author: delali
"""

from learning import *   


myData = DataSet(name = 'iris') 
AgentDT = DecisionTreeLearner(myData)
print("Prédiction en utilisant l'arbre de décision:") 
print("La Plante apprtient à la classe: "+ AgentDT([6.7,3.0,4.7,1.4])) 
myData.classes_to_numbers() 
classe=['setosa', 'versicolor', 'virginica']
AgentNN = NeuralNetLearner(myData,learning_rate=0.04, epochs=500)
cls=AgentNN([6.7,3.0,4.7,1.4])
print("Prédiction en utilisant le réseaux de neurones feedforward :")
print("La Plante apprtient à la classe: "+ str(cls)+": "+classe[cls]) 



