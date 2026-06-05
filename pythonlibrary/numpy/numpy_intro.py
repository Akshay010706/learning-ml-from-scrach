# make a python virtual environment 
#python -m venv .venv     --- this create virtual environment
#.venv\Scripts\activate.bat    --- this activate python environment
#deactivate -------- this deacivate python environment
#install numpy -- pip install numpy 

import numpy as np
from time import process_time

np_array = np.array([i for i in range(1000)])
starttime = process_time()
np_array +=5
endtime = process_time()
print(endtime-starttime)

# hence we use numpy for numerial operationn in python cause it is fast