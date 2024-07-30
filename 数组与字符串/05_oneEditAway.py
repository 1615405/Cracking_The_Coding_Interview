class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        lf, ls = len(first), len(second)
        if lf > ls:
            return self.oneEditAway(second, first)

        if ls - lf > 1:
            return False

        if ls == lf:
            count = 0
            for a, b in zip(first, second):
                count += (a != b)
            return count <= 1

        i, offset = 0, 0
        while i < lf:
            if first[i] != second[i + offset]:
                offset += 1
                if offset > 1:
                    return False
            else:
                i += 1
        return True
