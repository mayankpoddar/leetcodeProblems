class MinHeap:
    def __init__(self):
        self.minHeap = [-1]
        self.size = 0
    
    def parentIndex(self, index):
        return index // 2
    
    def leftChild(self, index):
        return 2*index
    
    def rightChild(self, index):
        return 2*index + 1
    
    def add(self, value, index):
        self.minHeap.append((value, index))
        self.size += 1
        current = self.size
        parent = self.parentIndex(current)
        while parent != 0 and self.minHeap[parent][0] > self.minHeap[current][0]:
            self.minHeap[parent], self.minHeap[current] = self.minHeap[current], self.minHeap[parent]
            current = parent
            parent = self.parentIndex(current)
    
    def removeMin(self):
        if self.size == 0:
            return None
        self.minHeap[1], self.minHeap[self.size] = self.minHeap[self.size], self.minHeap[1]
        minElement = self.minHeap.pop()
        self.size -= 1
        self.minHeapify(1)
        return minElement
    
    def minHeapify(self, index):
        lowest = index
        leftChild = self.leftChild(index)
        if leftChild <= self.size and self.minHeap[leftChild][0] < self.minHeap[lowest][0]:
            lowest = leftChild
        rightChild = self.rightChild(index)
        if rightChild <= self.size and self.minHeap[rightChild][0] < self.minHeap[lowest][0]:
            lowest = rightChild
        if lowest != index:
            self.minHeap[index], self.minHeap[lowest] = self.minHeap[lowest], self.minHeap[index]
            self.minHeapify(lowest)
        
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        mh = MinHeap()
        for i in range(n):
            mh.add(ratings[i], i)
        totalCandies = 0
        candiesDict = {}
        for i in range(n):
            candies = 0
            minElement = mh.removeMin()
            candies += 1
            neighbourCandies = 0
            leftIndex = minElement[1]-1
            if leftIndex >= 0:
                leftIndexElement = ratings[leftIndex]
                leftIndexCandies = candiesDict.get(leftIndex, None)
                if leftIndexCandies and leftIndexElement < minElement[0]:
                    neighbourCandies = leftIndexCandies
            rightIndex = minElement[1]+1
            if rightIndex <= n-1:
                rightIndexElement = ratings[rightIndex]
                rightIndexCandies = candiesDict.get(rightIndex, None)
                if rightIndexCandies and rightIndexElement < minElement[0]:
                    neighbourCandies = max(neighbourCandies, rightIndexCandies)
            candies += neighbourCandies
            candiesDict[minElement[1]] = candies
            totalCandies += candies
        return totalCandies
                    
                
                
                
        
        