class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rn_dict = {}
        mg_dict = {}

        for rn in ransomNote:
            if rn in rn_dict.keys():
                rn_dict[rn] = rn_dict[rn] + 1
            else:
                rn_dict[rn] = 1

        for mg in magazine:
            if mg in mg_dict.keys():
                mg_dict[mg] = mg_dict[mg] + 1
            else:
                mg_dict[mg] = 1

        ch_check_list = []

        for rn in rn_dict.keys():
            if rn in mg_dict.keys():
                if rn_dict[rn] <= mg_dict[rn]:
                    ch_check_list.append(True)
                else:
                    ch_check_list.append(False)
            else:
                return False


        print(f"rn_dict : {rn_dict}")
        print(f"mg_dict : {mg_dict}")
        print(f"ch_check_list : {ch_check_list}")

        if all(ch_check_list):
            return True
        else:
            return False
