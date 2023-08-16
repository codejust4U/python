import numpy as np
import random 
outcome = []
for i in range(10000):
    outcome.append(random.randint(1,6))


np.array(outcome).mean()


import numpy as np
import random 
outcome = []
for i in range(1000000):
    outcome.append(random.randint(1,6))


np.array(outcome).mean()


# above both code denotes that as much as the no of trials will be increased the expected outcome will be much more closer to the theoretical value