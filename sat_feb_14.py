class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        dp[0][0] = poured
        
        for r in range(query_row):
            for c in range(r + 1):
                if dp[r][c] > 1.0:
                    excess = (dp[r][c] - 1.0) / 2.0
                    dp[r + 1][c] += excess
                    dp[r + 1][c + 1] += excess
                    
        return min(1.0, dp[query_row][query_glass])