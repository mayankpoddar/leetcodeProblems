class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        toFind = image[sr][sc]
        if toFind == color:
            return image
        visited = [[False for i in range(n)] for j in range(m)]
        self.fillHelper(image, color, toFind, sr, sc, m, n, visited)
        return image
    
    def fillHelper(self, image, color, toFind, i, j, m, n, visited):
        visited[i][j] = True
        image[i][j] = color
        neighbors = [(i-1, j), (i, j+1), (i, j-1), (i+1, j)]
        for neighbor_i, neighbor_j in neighbors:
            if not (neighbor_i >= 0 and neighbor_i <= m-1 and neighbor_j >= 0 and neighbor_j <= n-1):
                continue
            print(i, j, neighbor_i, neighbor_j)
            if visited[neighbor_i][neighbor_j] == False and image[neighbor_i][neighbor_j] == toFind:
                self.fillHelper(image, color, toFind, neighbor_i, neighbor_j, m, n, visited)
    