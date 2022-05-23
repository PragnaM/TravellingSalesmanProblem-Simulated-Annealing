# TravellingSalesmanProblem-Simulated-Annealing

# Problem:
Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?

# Simulated Annealing:
Simulated annealing (SA) is an effective and general form of optimization, which is based on simulating the annealing of solids. “Annealing” refers to an analogy with thermodynamics, specifically with the way that metals cool and anneal. The simulated-annealing algorithm starts from a higher temperature, which is called the initial temperature. When the temperature gradually decreases, the solution of the algorithm tends to be stable. However, the solution may be a local optimal solution. To escape this local optimal solution a certain probability is calculated to find the global optimal solution.

# Working of the Program:
•	User enters the number of cities (N) </br>
•	Symmetric matrix of N x N is created with distances between each city being a random number.</br>
•	A random sequence of traversal is generated (population). </br>
•	Fitness Function- Calculates the sum of distances of each traversal. </br>
•	User enters Cooling Rate, Initial Temperature and Threshold values.</br>
</br>
•	SimulatedAnnealingFunction- Takes the population, coolingRate, initialTemperature, threshold as input parameters. </br>
    •	Calculate fitness of the initial sequence (previousdistance)</br>
    •	swapCities function- Takes the population and numberOfCitiesToSwap as input and returns a sequence of traversal where N cities are swapped. </br>
    •	Calculate the fitness of the new sequence (currentdistance)</br>
    •	If the currentdistance is less than the previousdistance</br>
    •	numberOfCitiesToSwap = numberOfCitiesToSwap * math.exp(-difference/(numberOfIterations*temperature)</br>
    •	Repeat this step 10 times after which the temperature is decreased as:</br>
        temperature = coolingRate * temperature</br>
    •	If currentdistance is not less than the previousdistance</br>
    •	Calculate the probability that the currentdistance would be accepted as:</br>
          Random number in range [0.0,1.0) < math.exp(-difference/temperature)</br>
    •	 numberOfCitiesToSwap = numberOfCitiesToSwap * math.exp(-difference/(numberOfIterations*temperature)</br>
•	Repeat until the numberOfIterations reaches threshold. </br>
</br>
•	For each iteration, a graph of fitness vs iteration is plotted which shows the decrease in the fitness as the number of iterations increases, and an optimal solution is obtained. </br>

