# Solution1: O(n^2) time | O(1) space
def twoNumberSum1(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

# Solution2 O(n) time | O(n) space
def twoNumberSum2(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

# Solution3 O(nlog(n)) | O(1) space
def twoNumberSum3(array, targetSum):
    array.sort()
    left, right = 0, len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

nums = [2,7,11,15]
target = 9
print(twoNumberSum1(nums,target))
print(twoNumberSum2(nums,target))
print(twoNumberSum3(nums,target))