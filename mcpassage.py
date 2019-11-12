import numpy as np
import matplotlib.pyplot as plt
import time

import utils

# Seed
#np.random.seed(42)


# Distribution and Brownian motion parameteres details
x0 = 0.0
D = 0.2
m = 0.0
s = np.sqrt(2 * D)

# Simulation params
T = 100 #End time of simulation
# We assume dt = 1
nTrajectory = 10000



# Generating and savin all trajectories
print("Generating trajectories...")
allTrajectory = utils.trajectoryGenerator(nTrajectory, T, m, s)






# The level to reach
levels = np.linspace(0.5, 0.6, 2)

allLevelResults = np.zeros((nTrajectory, T))
for idx, actLevel in enumerate(levels):
    #results = oneLevelStats(allTrajetory)
    allLevelResults[:, idx] = utils.oneLevelStats(allTrajectory, actLevel)
    
    


# Plot the histogram
results = allLevelResults[:, 0]
plt.hist(results[~np.isnan(results)], bins=range(T), density=True)

# Plot analitical passage density as end of simulation
tPoints = np.linspace(1, T, 100) 
p = utils.analyticSolution(actLevel, D, tPoints)
plt.plot(tPoints, p)
 

# Plot analitical Passage Time Density
plt.plot()
plt.show()


 


