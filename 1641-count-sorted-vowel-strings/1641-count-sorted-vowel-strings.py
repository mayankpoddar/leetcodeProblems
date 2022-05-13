class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        else:
            prev_matrix = [i for i in range(5, 0, -1)]
            for i in range(2, n+1):
                cum_sum = [0]*5
                cum_sum[4] = prev_matrix[4]
                for j in range(3, -1, -1):
                    cum_sum[j] = prev_matrix[j] + cum_sum[j+1]
                prev_matrix = cum_sum[:]
            return cum_sum[0]