import numpy as np
import matplotlib.pyplot as plt
import time

def firstPassageTime(level, trajectory):
    ''' Function to extract the forst passage information from one trajectory

    Input
    level: the level which we detect
    trajectory: numpy array storing the trajectory

    TODO: Think of more pythonic way to write this

    '''
        
    for idx in range(len(trajectory) - 1):
          if level >= 0:
              if trajectory[idx] < level and level < trajectory[idx+1]:
                  return idx + 1
          if level < 0: 
              if trajectory[idx] > level and level > trajectory[idx+1]:
                return idx + 1


def trajectoryGenerator(nTrajectory, T, m, s):
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


def analyticSolution(X, D, t):
    '''First passage time distribution

    The analytic curve as a benchmark for the numerical distribution

    '''
    tmp1 = X / np.sqrt(4 * np.pi * D * t**3)
    tmp2 = np.exp(- (X**2 / (4 * D * t))) 
    return tmp1 * tmp2


def oneLevelStats(allTrajectory, actLevel):
    ''' This function calculates the pass statistics for a given level '''

    # Array for results 
    nTrajectory = allTrajectory.shape[0]
    results = np.full(nTrajectory, fill_value=np.nan)

    numOfPassed = 0

    for actTrajectory in range(nTrajectory):
        passLevel = firstPassageTime(actLevel, allTrajectory[actTrajectory,:])
        if passLevel is not None:
            results[actTrajectory] = passLevel
            numOfPassed = numOfPassed + 1
        #else:
        #    print("Never reached")
    
    passFraction = numOfPassed/nTrajectory

    return results
 
 
 
 
