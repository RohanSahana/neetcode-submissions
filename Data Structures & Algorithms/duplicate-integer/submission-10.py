class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        seen = None
        for i in nums:
            if seen == i:
                return True
            else:
                seen = i
        return False