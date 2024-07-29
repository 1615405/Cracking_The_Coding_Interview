class Solution:
    def isUnique(self, astr: str) -> bool:
        move_bit = 0
        for char_s in astr:
            bit = ord(char_s) - ord('a')
            if move_bit >> bit & 1:
                return False
            move_bit |= (1 << bit)
        return True
