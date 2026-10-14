import re 
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        total_spaces = text.count(' ')
        if len(words) == 1:
            return words[0] + (' ' * total_spaces)
        spaces_between = total_spaces // (len(words) - 1)
        extra_spaces = total_spaces % (len(words) - 1)
        return (' ' * spaces_between).join(words) + (' ' * extra_spaces)
        