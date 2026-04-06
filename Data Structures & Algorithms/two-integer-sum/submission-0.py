class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map={}
        for i,n in enumerate(nums):
            check=target-n
            if check in n_map.keys():
                return [n_map[check],i]
            else:
                n_map[n]=i
        