class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_vol = 0

        while i < j:
            max_vol = max(max_vol, min(heights[i], heights[j]) * (j-i))
            if heights[i] < heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            elif heights[i] == heights[j]:
                i+=1
                j-=1
            
        
        return max_vol