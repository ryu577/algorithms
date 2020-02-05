import numpy as np
import pandas as pd
import heapq as hq


class Heap():
    def __init__(self):
        self.h_arr = []
        self.size = 0
    
    def pop(self):
        self.size-=1
        return hq.heappop(self.h_arr)

    def push(self,i):
        self.size += 1
        return hq.heappush(self.h_arr,i)

    def peak(self):
        if len(self.h_arr)>0:
            return hq.nsmallest(1,self.h_arr)[0]
        else:
            return np.inf

def down_intervals(starts, ends):
    heap = Heap()
    downs = []
    down = 0
    for i in range(len(starts)):
        while heap.size>0 and starts[i] > heap.peak():
            heap.pop()
            down-=1
            downs.append(down)
        heap.push(ends[i])
        down+=1
        downs.append(down)
    return downs


def complete_intervals(df):
    downs = down_intervals(df['start'],df['end'])
    all_intervals = np.sort(np.concatenate((df['start'],df['end']),axis=0))
    starts = all_intervals[1:]
    ends = all_intervals[:len(all_intervals)-1]
    d={'start':starts,'end':ends,'vms_down':downs}
    return pd.DataFrame(d)


def tst_case():
    vma_data = pd.DataFrame()
    d = {'start': [0,1,2,4,12], 'end': [10,3,6,5,13]}
    df = pd.DataFrame(data=d)
    return complete_intervals(df)

