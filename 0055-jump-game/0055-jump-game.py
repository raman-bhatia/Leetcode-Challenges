class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range (len(nums) - 1, -1 ,-1 ):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
"""
The range function takes three arguments: start, stop, and step. In this case, len(nums) - 1 is the start value, -1 is the stop value, and -1 is the step value.

The start value of len(nums) - 1 means that the loop will start at the last index of the list. The stop value of -1 means that the loop will continue until it reaches index -1, which is one before index 0. Since the stop value is not included in the range, this means that the loop will stop at index 0. The step value of -1 means that the loop will decrement by 1 on each iteration.

In summary, this for loop iterates over the indices of the list in reverse order, starting from the last index and going down to the first index. 
"""

        
        