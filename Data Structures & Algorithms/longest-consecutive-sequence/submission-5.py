class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num = set(nums)
        max_count = 1
        for i in num:
            if i-1 not in num:
                current_num = i
                current_streak = 1
                
                while current_num + 1 in num:
                    current_streak += 1
                    current_num += 1
                
                max_count = max(max_count, current_streak)
                    
                
        return max_count

                