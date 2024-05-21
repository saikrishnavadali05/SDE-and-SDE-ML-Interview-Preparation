class Solution:
    
    def isPalindrome_convert_to_str(self, x: int) -> bool:
        y = ''
        ch_str = str(x)

        for ch in ch_str:
            y = ch + y

        print(y)

        if ch_str == y:
            return True
        else:
            return False

# Your solution is on the right track with converting the integer to a string and comparing it with its reverse. Here are some hints for improvement:

# 1. **Avoid Extra Print Statements:** The `print(y)` statement is unnecessary for the final solution and can be removed.

# 2. **Simplify Reverse Logic:** You can simplify the logic for reversing the string by using Python slicing.

# 3. **Optimize for Edge Cases:** Consider how the solution handles negative numbers and edge cases like single-digit numbers. Negative numbers cannot be palindromes by definition.

# With these hints, you can refine your solution further.

# Based on your solution, I would give you a 7 out of 10. Here's the breakdown:

# - **Correct Logic (4/5):** Your logic for converting the integer to a string and comparing it with its reverse is correct.
# - **Efficiency (2/3):** Your method of reversing the string can be simplified for better readability and efficiency.
# - **Edge Case Handling (1/2):** You need to account for edge cases like negative numbers more explicitly.

# Overall, your approach is sound but can be optimized and refined.

    #optimised solution
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else:
            remaining_num = x
            reversed_num = ''
            while(remaining_num >= 10):
                last_digit_ch = str(remaining_num % 10) 
                remaining_num = x // 10

                reversed_num = reversed_num + last_digit_ch

            reversed_num = remaining_num + reversed_num

            reversed_num = int(reversed_num)

            if reversed_num == x:
                return True
            else:
                return False

                
