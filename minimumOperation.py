class Solution:
    def minimumOperations(self, nums):
        result = 0
        for i in nums:
            if i%3==0:
                continue
            elif (i+1) % 3==0:
                result +=1
            elif ((i-1) % 3 == 0):
                result +=1
            else:
                continue
        return result
if __name__ == '__main__':
    q1 = Solution()
    nums = [1,2,3,4]
    print(q1.minimumOperations(nums))