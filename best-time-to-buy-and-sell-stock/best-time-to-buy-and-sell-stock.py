class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=prices[0]
        p=0
        for i in range(1,len(prices)):
            s=prices[i]
            if s>b:
                p=max(s-b,p)
            elif s<b:
                b=s
        return p