import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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
resolution = 1
maxLevel = 10
minLevel = -maxLevel
nLevel = 2 * (maxLevel / resolution) + 1

# DataFrame for the raw simulation data
# Columns:  One column for each simulated trajectory (sample)
# Rows:     One row for every level which passage is registered for
# Value:    First passage time for a given trajectory (column) and a given level (row)
#           Nan means the level was never passed
raw = pd.DataFrame()
raw = raw.reindex(columns = range(nSample))
raw['levels'] = np.linspace(minLevel, maxLevel, nLevel)  
#raw = raw.set_index('levels')
#print(raw)

# Generating trajectories
for sample in range(nSample):
  x = 0.0
  trajectory = np.empty(simLength)
  for actTime in range(simLength):
    x = x + np.random.normal(mu, sigma * np.sqrt(dt))

    trajectory[actTime] = x

    if(x >= 0):
      # Index of largest level smaller than act value (level just passed from below)
      levelIndex = raw[raw['levels'] <= x].index[-1]
    else:
      # Index of smalles level larger than act value (level just passed from ebove)
      levelIndex = raw[raw['levels'] >= x].index[0]

    passageTime = raw.at[levelIndex, sample]
    #print(x, sample, levelIndex, passageTime)
    if(np.isnan(passageTime)):
      raw.at[levelIndex, sample] = actTime

  for idx, val in enumerate(trajectory):
    print(idx, val)


print(raw)
exit(0)


    
    


#plt.plot(B)
#plt.show()


