class Solution:
def minFlips(self, s: str) -> int:
    n = len(s)
    s = s + s


    # alternating patterns
    pattern_1 = "".join('0' if i % 2 == 0 else '1' for i in range(2*n))
    pattern_2 = "".join('1' if i % 2 == 0 else '0' for i in range(2*n))

    diff1 = diff2 = left = 0
    ans = float('inf')

    for right in range(2*n):

        if s[right] != pattern_1[right]:
            diff1 += 1
        if s[right] != pattern_2[right]:
            diff2 += 1

        if right - left + 1 > n: #ths will correctly calculate the next index
            if s[left] != pattern_1[left]:
                diff1 -= 1
            if s[left] != pattern_2[left]:
                diff2 -= 1
            left += 1

        if right - left + 1 == n:
            ans = min(ans, diff1, diff2)

    return ans
