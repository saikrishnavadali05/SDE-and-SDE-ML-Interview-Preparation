# Actual Solution

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Counter for the number of elements not equal to val
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k
    
    
# My Attempt

# Your solution has a few logical issues and inefficiencies. Here's a breakdown of the problems and suggestions for improvement:

# Use of Extra Lists: Maintaining val_indices and indices_covered adds unnecessary complexity and space usage.

# Incorrect Logic: The second for loop and the logic inside it do not correctly handle removing elements and shifting the remaining elements.

# Efficiency: Your solution has an inefficient time complexity due to the nested loops and the way you handle the indices.

# Given your effort and the initial structure of your solution, I would rate your solution a 6 out of 10. Here's a detailed breakdown:

# Effort and Structure (4/4): You made a good attempt and had a clear structure in your code.
# Logic (1/4): The logic had several issues and inefficiencies, such as unnecessary lists and incorrect handling of element removal.
# Efficiency (1/2): The solution is not efficient in terms of time and space complexity.
# What You Did Well:
# Structured Approach: You clearly defined a class and method, showing an understanding of object-oriented programming.
# Initialization: Properly initialized variables and set up loops to iterate through the list.
# Areas for Improvement:
# Correctness: The logic for removing elements and shifting remaining elements was not implemented correctly.
# Efficiency: The use of extra lists and nested loops resulted in suboptimal time complexity and unnecessary space usage.
# With a few improvements, particularly in understanding the logic required for in-place modification of the list, you can significantly enhance your solution. Keep practicing, and you'll get better at identifying and correcting these kinds of issues!


#   class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         nums_length = len(nums)
#         val_indices = []
#         k = nums_length

#         for idx, n in enumerate(nums, start=0):
#             if n == val:
#                 val_indices.append(idx)
#                 k = k - 1

#         for idx in range(k - 1, nums_length):
#             indices_covered = []
#             if nums[idx] == val:
#                 for i in range(k, len(nums)):
#                     if i in indices_covered:
#                         continue
#                     else:
#                         nums[idx] = nums[i]
#                         indices_covered.append(i)
        
#         return k

# # Example usage:
# nums1 = [3, 2, 2, 3]
# val1 = 3
# solution = Solution()
# k1 = solution.removeElement(nums1, val1)
# print(f"k: {k1}")
# print(f"nums: {nums1}")

# nums2 = [0, 1, 2, 2, 3, 8, 4, 2]
# val2 = 2
# k2 = solution.removeElement(nums2, val2)
# print(f"k: {k2}")
# print(f"nums: {nums2}")
