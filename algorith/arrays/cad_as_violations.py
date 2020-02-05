import numpy as np
import pandas as pd
import heapq as hq

vma_data = pd.DataFrame()

d = {'start': [0,1,2,4,12], 'end': [10,3,6,5,13]}
df = pd.DataFrame(data=d)

starts = df['start']
ends = df['ends']

heap = []
downs = []

for i in range(len(starts)):
    hq.heappush(heap,ends[i])
    h_peak = hq.nsmallest(1,heap)[0]
    
