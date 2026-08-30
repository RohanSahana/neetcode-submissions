class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for idx,i in enumerate(nums):
            if i not in hm:
                hm.update({target - i : idx})
            else:
                return [hm.get(i), idx]
        
        # for idx2,j in enumerate(nums):
        #         if idx1 == idx2:
        #             continue
        #         if i + j == target:
        #             return [idx1,idx2]