class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = {}
        all_profits = []
        max_found_so_far = 0
        for day_idx, check_price in enumerate(prices, start = 0):
            for next_price in prices[day_idx+1:]:
                if next_price < check_price:
                    continue
                    
                cost_diff = next_price - check_price
                if cost_diff > max_found_so_far:
                    max_found_so_far = cost_diff
                    
            #     all_profits.append(cost_diff)

            # profits[day_idx] = all_profits
            # all_profits = [] 
        # print(f"profits : {profits}")
        print(f"max_found_so_far : {max_found_so_far}")

        # max_found_so_far = 0
        # max_idx = 0
        # for key in profits.keys():
        #     for ele in profits[key]:
        #         if ele > max_found_so_far:
        #             max_found_so_far = ele
        #             max_idx = key

        # print(f"max_found_so_far : {max_found_so_far}")
        # print(f"max_idx : {max_idx + 1}")
        return max_found_so_far
