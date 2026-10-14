import re 
class Solution:
    def reorderSpaces(self, text: str) -> str:
        no_spaces = 0
        no_words = 0
        lst = re.findall(r"\S+|\s", text)
        for st in lst:
            if st == " ":
                no_spaces += 1
            else:
                no_words += 1
        strs_lst = [item for item in lst if item != " "]
        if no_words == 1:
            return strs_lst[0] + (" " * no_spaces)
        cal = no_spaces // (no_words - 1)
        flag = True if no_spaces % (no_words -1) != 0 else False
        res = strs_lst[0]
        for s in strs_lst[1:]:
            res += (" "*cal) + s
            
        if flag:
            res += " "*(no_spaces % (no_words - 1))

        return res