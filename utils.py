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
 
