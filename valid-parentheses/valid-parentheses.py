class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        if len(s)%2 == 1:
            return False
        braces = {"}":"{","]":"[",")":"("}
        for c in s:
            if c in braces.values():
                arr.append(c)
            elif c in braces.keys():
                if arr == [] or braces[c]!=arr.pop():
                    return False
            else:
                return False
        return arr == []
        