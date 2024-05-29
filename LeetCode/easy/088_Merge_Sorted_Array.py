# CHATGPT Reference Code

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
        


#         # Initialize three pointers
#         p1 = m - 1  # Pointer for the last element in nums1's valid part
#         p2 = n - 1  # Pointer for the last element in nums2
#         p = m + n - 1  # Pointer for the last position in nums1
        
#         # Merge nums2 into nums1 from the end to the beginning
#         while p1 >= 0 and p2 >= 0:
#             if nums1[p1] > nums2[p2]:
#                 nums1[p] = nums1[p1]
#                 p1 -= 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 -= 1
#             p -= 1
        
#         # If there are any remaining elements in nums2, copy them
#         nums1[:p2 + 1] = nums2[:p2 + 1]

# -----------------------------------------------------------------------------------



# Attempt 1 (bored)
class Solution:

    def shift_num1_elements(num1, shift_pos):
        for i range()

    # trial 1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i, n1 in enumerate(nums1, start=0):
            for j, n2 in enumerate(nums2, start=0):

                if nums1[i] < nums2[j]:
                    nums1[i + 1] = nums2[j] 
                
                if nums1[i] > nums2[j]:
                    nums1[i + 1] = nums1[i]
                    nums1[i] = nums2[j]

                if nums1[i] == nums2[j]:
                    nums1[i + 1] = nums2[j]

        return None

    #trial 2
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #         """
    #         Do not return anything, modify nums1 in-place instead.
    #         """
    #         j = 0
    #         while(1):
    #             if nums1[i] < nums2[j]:
    #                 i = i+1
                
    #             elif nums1[i] == nums2[j]:
    #                 nums1[i + 1] = nums2[j]
    #                 i = i + 1
    #                 j = j + 1
    
    #                 for k, n1 in enumerate(nums1[i:0], start=0):
    #                     nums1[k + 1]
    
    #             elif nums1[i] > nums2[j]:
    #                 nums1[i + 1] = nums2[j]
    
    #         return None
    
