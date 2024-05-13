import math
import sys

class Solution:

    @staticmethod
    def check_constraints(nums):
        if ((2 <= len(nums)) & (len(nums) <= math.pow(10, 4))):
            return True
        else:
            print("invalid input array")
            sys.exit(0)


    @staticmethod
    def element_check_constraint(element):
        if math.pow(-10, 9) <= element & element <= math.pow(10, 9):
            return True
        else:
            return False

    @staticmethod
    def twoSum(nums, target):
        print(f"nums :{nums}")
        print(f"target :{target}")

        if not Solution.element_check_constraint(target):
            sys.exit(0)

        elif not Solution.check_constraints(nums):
            sys.exit(0)

        else:
            for ele1_idx, ele1 in enumerate(nums, start=0):
                for ele2_idx, ele2 in enumerate(nums[1:], start=1):

                    if Solution.element_check_constraint(ele1) & Solution.element_check_constraint(ele2):
                        if ele1 + ele2 == target:
                            return [ele1_idx, ele2_idx]
                        else:
                            continue
                    else:
                        print("invalid input")


if __name__ == "__main__":

    # nums = [1]
    # target = 1

    # print(f"sum indices : {Solution.twoSum(nums, target)}")

    nums = [2,7,11,15]
    target = 9

    print(f"sum indices : {Solution.twoSum(nums, target)}")

    nums = [3,2,4]
    target = 6

    print(f"sum indices : {Solution.twoSum(nums, target)}")

    nums = [3,3]
    target = 6
    print(f"sum indices : {Solution.twoSum(nums, target)}")