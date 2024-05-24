class Solution:
    def romanToInt(self, s: str) -> int:

        replace_dict = {
            "I"      :       "1",
            "V"      :       "5",
            "X"       :      "10",
            "L"       :      "50",
            "C"        :     "100",
            "D"        :     "500",
            "M"         :    "1000",
        }


        subtract_dict = {
            'IV' : '4',
            'IX' : '9',
            'XL' : '40',
            'XC' : '90',
            'CD' : '400',
            'CM' : '900'
        } 

        s_num = s

        for key in subtract_dict.keys():
            if key in s:
                s_num = s_num.replace(key, f'<{str(subtract_dict[key])}>')

        for key in replace_dict.keys():
            if key in s_num:
                s_num = s_num.replace(key, f'<{str(replace_dict[key])}>')
        
        s_num = s_num.replace("><", "+")
        s_num = s_num.replace("<", "").replace(">", "")

        s_num_list = s_num.split("+")

        final_num = 0
        for num_str in s_num_list:
            final_num = int(num_str) +  final_num

        print(final_num)

        return final_num
