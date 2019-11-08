import numpy as np
import matplotlib.pyplot as plt
import time

# Seed
#np.random.seed(42)


def fpass(trh, arr):
    ''' Function to extract the forst passage information from one trajectory

    Input
    trh: the level which we detect
    arr: numpy array storing the trajectory

    TODO: Think of more pythonic way to write this

    '''
        
    for idx in range(len(arr) - 1):
          if trh >= 0:
              if arr[idx] < trh and trh < arr[idx+1]:
                  return idx + 1
          if trh < 0: 
              if arr[idx] > trh and trh > arr[idx+1]:
                return idx + 1


def fptd(X, D, t):
    '''First passage time distribution

    The analytic curve as a benchmark for the numerical distribution

    '''
    tmp1 = X / np.sqrt(4 * np.pi * D * t**3)
    tmp2 = np.exp(- (X**2 / (4 * D * t))) 
    return tmp1 * tmp2

def trajectoryGenerator(nTrajectory, T):
    ''' Function that generates trajectories

    nTrajectories: number
    T: length

    '''
     
    genStart = time.time()
    allTrajectory = np.full((nTrajectory, T), np.nan)
    
    for actTrajectory in range(nTrajectory):
        allTrajectory[actTrajectory, 0] = 0.0
        for i in range(T - 1):
            allTrajectory[actTrajectory, i + 1] = allTrajectory[actTrajectory, i] + np.random.normal(m, s)
    
    genEnd = time.time()

    print(str(nTrajectory) + " trajectories generated in " + str(genEnd - genStart) + " seconds.")

    # Check trajectories by sight
    # plt.plot(np.transpose(allTrajectory))
    # plt.show()
 

    return allTrajectory
 

# Distribution and Brownian motion parameteres details
x0 = 0.0
D = 0.2
m = 0.0
s = np.sqrt(2 * D)

# Simulation params
T = 100 #End time of simulation
# We assume dt = 1
nTrajectory = 10000

# The level to reach
actLevel = 0.5


allTrajectory = trajectoryGenerator(nTrajectory, T)







results = np.full(nTrajectory, fill_value=np.nan)
numOfPassed = 0
for actTrajectory in range(nTrajectory):


  passLevel = fpass(actLevel, allTrajectory[actTrajectory,:])
  #print("passLevel ",passLevel)
  if passLevel is not None:
    results[actTrajectory] = passLevel
    numOfPassed = numOfPassed + 1
  #else:
  #  print("Never reached")

print("Fraction passed: ", numOfPassed/nTrajectory)


# Plot the histogram
plt.hist(results[~np.isnan(results)], bins=range(T), density=True)

# Plot analitical passage density as end of simulation
tPoints = np.linspace(1, T, 100) 
p = fptd(actLevel, D, tPoints)
plt.plot(tPoints, p)
 

# Plot analitical Passage Time Density
plt.plot()
plt.show()


 


