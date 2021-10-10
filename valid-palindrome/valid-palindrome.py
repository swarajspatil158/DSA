class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for i in s:
            if i.isalnum():
                new_str+=i
        length = len(new_str)//2
        for i in range(length):
            if new_str[i].lower() != new_str[-i-1].lower():
                print(new_str[i],new_str[-i-1])
                return False
        return True
            