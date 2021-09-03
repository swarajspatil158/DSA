class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_units=0
        b = sorted(boxTypes, key=lambda boxTypes:boxTypes[1])
        for i in range(len(b)-1,-1,-1):
            if truckSize > b[i][0]:
                truckSize-=b[i][0]                
                max_units+=b[i][1]*b[i][0]
            else:
                max_units+=truckSize*b[i][1]
                break
        return max_units
                