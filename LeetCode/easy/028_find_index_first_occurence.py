# working solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        needle_length = len(needle)
        hay_length = len(haystack)

        print(f"needle_length : {needle_length}")
        print(f"hay_length : {hay_length}")

        for hay_chidx, hay_ch in enumerate(haystack, start=0):
            # print(f"hay_ch : {hay_ch}")
            # print(f"hay_chidx : {hay_chidx}")
            hay_sub_str = haystack[hay_chidx:]
            # print(f"hay_sub_str : {hay_sub_str}")
            
            if hay_ch == needle[0]:
                # hay_substr = haystack[hay_chidx : needle_length]
                # chatgpt changed this line to the below line and it solved the code
                # I need to improve slicing in python, next. 
                hay_substr = haystack[hay_chidx : hay_chidx+needle_length]
                # print(f"hay_substr : {hay_substr}")
                if hay_substr:
                    if hay_substr == needle:
                        return hay_chidx
                # elif hay_chidx + 1 == hay_length:
                #     print("Reached the end of haystack, searched for all characters")
                #     return -1
                else:
                    continue

            elif len(hay_sub_str) == needle_length:
                print("checking for final sub string in hay, whose length is same as needle")
                if hay_sub_str == needle:
                    return hay_chidx
                else:
                    return -1


        return -1
# ====================================================================

# Based on your initial implementation of the `strStr` function, I would give you a 7 out of 10. Here’s the breakdown:

# 1. **Understanding of the Problem**: You understood the problem and attempted to solve it using string slicing and comparison, which is a good approach.
# 2. **Effort and Logic**: You made an effort to iterate through the `haystack` and compare substrings, showing that you understand the need to find the starting index of the `needle`.
# 3. **Use of Enumerate**: While `enumerate` can be useful, it wasn't necessary in this context. Your logic had some redundancies and potential issues that could lead to incorrect results.

# ### Areas for Improvement:
# 1. **Simplification**: The solution could be simplified by directly comparing substrings without additional slicing.
# 2. **Edge Cases**: Handling the edge case where `needle` is an empty string was missing.
# 3. **Efficiency**: The use of slicing in multiple places can be inefficient. Simplifying the loop and comparisons improves performance and readability.

# Overall, your approach shows a good grasp of basic string manipulation and iteration, but refining your logic and considering edge cases can help make your solution more robust and efficient.

# my try
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:

#         needle_length = len(needle)
#         hay_length = len(haystack)

#         for hay_chidx, hay_ch in enumerate(haystack, start=0):
            
#             hay_sub_str = haystack[hay_chidx:]
            
#             if hay_ch == needle[0]:
#                 hay_substr = haystack[hay_chidx : needle_length]
#                 print(f"hay_substr : {hay_substr}")
#                 if hay_substr:
#                     if hay_substr == needle:
#                         return hay_chidx
#                 # elif hay_chidx + 1 == hay_length:
#                 #     print("Reached the end of haystack, searched for all characters")
#                 #     return -1
#                 else:
#                     continue

#             elif len(hay_sub_str) == needle_length:
#                 print("checking for final sub string in hay, whose length is same as needle")
#                 if hay_sub_str == needle:
#                     return hay_chidx
#                 else:
#                     return -1

            
            



# ===================================================================================
# code worked, accepted. straight forward approach. use inbuilt function
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         # haystack = "is great sai"
#         # needle = "sai"
#         index = haystack.find(needle)
#         print(f"index : {index}")

#         return index
