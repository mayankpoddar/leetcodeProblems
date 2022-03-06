class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        amounts = [[-1 for i in range(100)] for j in range(100)]
        excess = [[0 for i in range(100)] for j in range(100)]
        for i in range(100):
            for j in range(i+1):
                amounts[i][j] = 0
        for i in range(100):
            for j in range(100):
                if i == 0:
                    if poured >= 1:
                        amounts[i][0] = 1
                        excess[i][0] = poured - 1
                else:
                    above = excess[i-1][j]
                    aboveLeft = 0 if j < 1 else excess[i-1][j-1]
                    totalAmount = 0.5*above + 0.5*aboveLeft
                    if totalAmount >= 1:
                        amounts[i][j] = 1
                        excess[i][j] = totalAmount - 1
                    else:
                        amounts[i][j] = totalAmount
        return (1.0*amounts[query_row][query_glass])
                    
        