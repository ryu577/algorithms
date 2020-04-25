class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        # First get the max height
        max_ht=max(height); area = 0
        potential = np.zeros(max_ht); max_h_so_far = 0
        prev_ht = 0
        ## Now start collecting rain.
        for h in height:
            for j in range(h, max_h_so_far):
                potential[j]+=1
            
            for j in range(prev_ht,h):
                area += potential[j]
                potential[j] = 0
        
            if h > max_h_so_far:
                max_h_so_far = h
            
            prev_ht = h            
                            
        return int(area)
  
  
