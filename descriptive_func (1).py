#take mean, mad, sd, mad median, and sem 
#writtenBy = "Jessica Merritt"

import numpy as np
#importing function from file
from mad_funcMerritt import mad_func

def descriptive_func(x):
    #run an empty array to assign mad 
    mad = np.empty([len(x),1])
    mad[:]=np.NaN
#%%
    #enter for loop to iterate over array 
    for i in range(len(x)):
        #calculate mean, median and std
        mean = np.mean(x, axis=0)
        median = np.median(x, axis=0)
        std = float(np.std(x, axis=0))
        #take length of array to use to calculate the sem
        length = len(x)
        mad = float(mad_func(x))
        #take std and length of array for sem
        sem = float(std / np.sqrt(length))
        #return output to the user 
    return mean, median, length, std, mad, sem




