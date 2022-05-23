# -*- coding: utf-8 -*-
"""

@author: Pragna M
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import math 

#Calculate fitness
def fitnessFunction(population):
    fitness=0
    for i in range(0,numberOfCities-1):
            city1= population[i]
            city2= population[i+1]
            fitness = fitness + distancematrix[city1,city2] #sum of distances from city1 to cityN
        
    lastcity=population[-1]
    firstcity= population[0]
    fitness= fitness+ distancematrix[lastcity,firstcity] #Distance from cityN back to city1

    fitness=1/fitness
    return fitness

def swapCities(population, numberOfCities):
  for i in range (0,numberOfCities+1):
    cityswap1=random.randint(0,numberOfCities-1)
    cityswap2=random.randint(0,numberOfCities-1)
    if (cityswap1 == cityswap2):  # check if random indexes are equal
        cityswap2 = cityswap1 - 1
        
    swap=population[cityswap1]
    population[cityswap1]=population[cityswap2]
    population[cityswap2]=swap
  return population

def simulatedannealing(population, initialTemperature, coolingRate, threshold, numberOfCitiesToSwap):
    numberOfIterations = 1
    temperature= initialTemperature
    #initialCitiesToSwap= numberOfCitiesToSwap
    completeTemperatureIterations= 0
    xaxis=[]
    yaxis=[]
    minfitness=[]
    
    while numberOfIterations < threshold:
        previousdistance= fitnessFunction(population)
        temp_cities= swapCities(population,numberOfCitiesToSwap)
        if numberOfIterations == 1:
            currentdistance= previousdistance
            difference = 0
            minfitness.append(currentdistance)

        else:
            currentdistance= fitnessFunction(temp_cities)
            difference = abs(currentdistance - previousdistance)
        #print(difference)
        if currentdistance < previousdistance:
            population= temp_cities
            if completeTemperatureIterations >= 10: #take min distance
                temperature = coolingRate * temperature
                completeTemperatureIterations = 0
               
            numberOfCitiesToSwap=int(round(numberOfCitiesToSwap * math.exp(-difference/(numberOfIterations*temperature))))
            #print (numberOfCitiesToSwap)
            if numberOfCitiesToSwap == 0:
                numberOfCitiesToSwap = 1
                
            numberOfIterations = numberOfIterations + 1
            completeTemperatureIterations = completeTemperatureIterations + 1
            minfitness.append(currentdistance)
            #print(minfitness)
            #print(currentdistance)
            #print("Fitness in this iteration:", currentdistance)
            yaxis.append(1/currentdistance)
            #print("Iteration:", numberOfIterations)
            xaxis.append(numberOfIterations)

        else:
                if random.random() < math.exp(-difference/temperature):
                    population = temp_cities
                    numberOfCitiesToSwap= int( numberOfCitiesToSwap * math.exp(-difference/(numberOfIterations*temperature)))
                    if numberOfCitiesToSwap == 0:
                        numberOfCitiesToSwap = 1
                numberOfIterations = numberOfIterations + 1
                completeTemperatureIterations = completeTemperatureIterations + 1
                #print("Fitness in this iteration:", previousdistance)
                yaxis.append(1/previousdistance)
                #print("Iteration:", numberOfIterations)
                xaxis.append(numberOfIterations)

        
        print ("Iterations: ",numberOfIterations)
        print ("Temperature:", temperature)
        print ("In current temperature for:", completeTemperatureIterations, "times")
    plt.plot(xaxis,yaxis)
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.show()
    return previousdistance                
        
#Generate dataset in matrix format
numberOfCities = int(input("Enter number of Cities:"))  # size of matrix
distancematrixhalf = np.random.randint(0,100,size=(numberOfCities,numberOfCities)) # random symmetric matrix
distancematrix = (distancematrixhalf + distancematrixhalf.T)
for i in range (0,numberOfCities):
    distancematrix[i][i]=0 # diagonal elements=0
print (distancematrix)

population=random.sample(range(0, numberOfCities), numberOfCities)    

print (population)      



#Get fitness of initial population
fitness= fitnessFunction(population)

coolingRate= float(input("Enter Cooling Rate (less than 1):" ))
if coolingRate > 1:
    coolingRate= float(input("Enter Cooling Rate (less than 1):" ))
initialTemperature= float(input("Enter initial Temperature:" ))
threshold= int(input("Enter Threshold:" ))
numberOfCitiesToSwap= numberOfCities

simulatedannealing(population, initialTemperature, coolingRate, threshold, numberOfCitiesToSwap)
