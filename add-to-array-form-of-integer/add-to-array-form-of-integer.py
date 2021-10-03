class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = [str(integer) for integer in num]
        number = int(''.join(num))
        number=str(number+k)
        number = [number[idx] for idx in range(0, len(number))]
        return number
                             