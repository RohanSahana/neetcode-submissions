class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        count = 2
        while count > 0:
            ans.extend(nums)
            count -= 1
        return ans
            