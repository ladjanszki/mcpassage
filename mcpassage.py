import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Seed
# np.random.seed(42)

# Print all rows from a dataframe
# pd.set_option('display.max_rows', None)

# First occurence
def fpass(trh, arr):
  for idx in range(len(arr) - 1):
      if trh >= 0:
        if arr[idx] < trh and trh < arr[idx+1]:
          return idx + 1
      if trh < 0: 
        if arr[idx] > trh and trh > arr[idx+1]:
          return idx + 1
 

# Distribution details
mu = 0.0
sigma = 0.1

# Simulation params
simLength = 10

# The level to reach
actLevel = 0.1

# Generating a path
trajectory = np.empty(simLength)
trajectory[0] = 0.0
for i in range(simLength - 1):
  trajectory [i + 1] = trajectory[i] + np.random.normal(mu, sigma)

for idx, val in enumerate(trajectory):
  print(idx, val)

# plt.plot(trajectory)
# plt.show()

print("--------------------------------")

print(actLevel, fpass(actLevel, trajectory))



exit(0)

maxIndex = 20 # TODO: pick the middle val by expression
minIndex = 20
x = 0.0
for i in range(20):
  x = x + np.random.normal(0, 0.5)

  if(x >= 0):
    # Index of largest level smaller than act value (level just passed from below)
    indices = np.where(levels < x)
 






# Print all rows from a dataframe
pd.set_option('display.max_rows', None)

# Distribution details
mu = 0.0
sigma = 0.25
dt = 1

# Simulation params
simLength = 100
nSample = 1

# Levels to reach
resolution = 0.1
maxLevel = 2
minLevel = -maxLevel
nLevel = 2 * (maxLevel / resolution) + 1



levels = np.linspace(minLevel, maxLevel, nLevel)  
for idx, val in enumerate(levels):
  print(idx, val)


maxIndex = 20 # TODO: pick the middle val by expression
minIndex = 20
x = 0.0
for i in range(20):
  x = x + np.random.normal(0, 0.5)

  if(x >= 0):
    # Index of largest level smaller than act value (level just passed from below)
    indices = np.where(levels < x)
    index = indices[0][-1]
    print(x, indices[0][-1])
    if index > maxIndex:
        print("new max")
        maxIndex = index

  else:
    # Index of smalles level larger than act value (level just passed from ebove)
    indices = np.where(levels > x)
    index = indices[0][0]
    print(x, indices[0][0])
    if index < minIndex:
      print("new min")
      minIndex = index
 
  


exit(0)






# DataFrame for the raw simulation data
# Columns:  One column for each simulated trajectory (sample)
# Rows:     One row for every level which passage is registered for
# Value:    First passage time for a given trajectory (column) and a given level (row)
#           Nan means the level was never passed
raw = pd.DataFrame()
#raw = raw.reindex(columns = range(nSample))
raw = raw.reindex(columns = range(simLength))
raw['levels'] = np.linspace(minLevel, maxLevel, nLevel)  
raw = raw.fillna(0)
#raw = raw.set_index('levels')
#print(raw)

# Generating trajectories
for sample in range(nSample):
  x = 0.0
  #trajectory = np.empty(simLength)
  for actTime in range(simLength):
    x = x + np.random.normal(mu, sigma * np.sqrt(dt))

    #trajectory[actTime] = x

    if(x >= 0):
      # Index of largest level smaller than act value (level just passed from below)
      levelIndex = raw[raw['levels'] <= x].index[-1]
    else:
      # Index of smalles level larger than act value (level just passed from ebove)
      levelIndex = raw[raw['levels'] >= x].index[0]

    #passageTime = raw.at[levelIndex, sample]
    ##print(x, sample, levelIndex, passageTime)
    #if(np.isnan(passageTime)):
    #  raw.at[levelIndex, sample] = actTime
    raw.at[levelIndex, actTime] = raw.at[levelIndex, actTime] + 1

 # for idx, val in enumerate(trajectory):
 #   print(idx, val)


print(raw)
exit(0)


    
    


#plt.plot(B)
#plt.show()


