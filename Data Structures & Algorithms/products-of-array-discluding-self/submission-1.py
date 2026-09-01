class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans = [1]*len(nums)
        #left
        for idx in range(1,n):
            ans[idx] = ans[idx-1] * nums[idx-1]
        #right
        rp = 1
        for idx in range(n-1, -1, -1):
            ans[idx] = ans[idx] * rp
            rp *= nums[idx]

        return ans
