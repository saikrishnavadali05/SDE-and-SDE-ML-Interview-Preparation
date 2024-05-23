class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_occ_dict = {}
        for ele in nums:
            if ele in num_occ_dict.keys():
                num_occ_dict[ele] = num_occ_dict[ele] + 1
            else:
                num_occ_dict[ele] = 1

        for ele_num, occ_count in num_occ_dict.items():
            if occ_count > len(nums) // 2 :
                return ele_num 
