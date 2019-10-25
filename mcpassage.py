import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Seed
#np.random.seed(42)

# Print all rows from a dataframe
# pd.set_option('display.max_rows', None)

# First occurence
# TODO Think of better way to get index
def fpass(trh, arr):
  for idx in range(len(arr) - 1):
      if trh >= 0:
        if arr[idx] < trh and trh < arr[idx+1]:
          return idx + 1
      if trh < 0: 
        if arr[idx] > trh and trh > arr[idx+1]:
          return idx + 1

#def fptd(X, xc, x0, D, t):
#  ''' Function to calculate the analitican first passage time density'''
#  tmp1 = 1.0 / np.sqrt(4 * np.pi * D * t)
#  tmp2 = np.exp(- (X - x0)**2 / (4 * D * t)) 
#  tmp3 = np.exp(- (X - (2 * xc - x0))**2 / (4 * D * t)) 
#  return tmp1 * (tmp2 - tmp3)

def fptd(X, D, t):
  '''First passage time distribution'''
  tmp1 = X / np.sqrt(4 * np.pi * D * t**3)
  tmp2 = np.exp(- (X**2 / (4 * D * t))) 
  return tmp1 * tmp2
 



# Distribution and Brownian motion parameteres details
x0 = 0.0
D = 0.2
m = 0.0
s = np.sqrt(2 * D)

# Simulation params
T = 100 #End time of simulation
# We assume dt = 1
nTrajectory = 100000

# The level to reach
actLevel = 0.5


results = np.full(nTrajectory, fill_value=np.nan)
numOfPassed = 0
for actTrajectory in range(nTrajectory):
  # Generating a path
  trajectory = np.empty(T)
  trajectory[0] = 0.0
  for i in range(T - 1):
    trajectory [i + 1] = trajectory[i] + np.random.normal(m, s)
  
  #for idx, val in enumerate(trajectory):
  #  print(idx, val)
  
  # plt.plot(trajectory)
  # plt.show()
  
  # print("--------------------------------")
  #print(actLevel, fpass(actLevel, trajectory))

  passLevel = fpass(actLevel, trajectory)
  #print("passLevel ",passLevel)
  if passLevel is not None:
    results[actTrajectory] = passLevel
    numOfPassed = numOfPassed + 1
  #else:
  #  print("Never reached")

print("Fraction passed: ", numOfPassed/nTrajectory)


#print("#####")
#print(results)
#print("#####")


# Printing out the histogram values
#hist, bins = np.histogram(results[~np.isnan(results)], bins=range(T), density=True)
#print(hist) 
#print(bins)


# Plot the histogram
plt.hist(results[~np.isnan(results)], bins=range(T), density=True)

# Plot analitical passage density as end of simulation
tPoints = np.linspace(0, T, 100) 
p = fptd(actLevel, D, tPoints)
plt.plot(tPoints, p)
 

# Plot analitical Passage Time Density
plt.plot()
plt.show()



