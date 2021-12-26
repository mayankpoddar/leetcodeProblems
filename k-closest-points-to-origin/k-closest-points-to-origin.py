import math

class Node:
    def __init__(self, x=None, y=None, distance=None):
        self.point = [x, y]
        self.distance = distance
    def __str__(self):
        return str(self.point) + " || " + str(self.distance)

class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def size(self):
        return len(self.heap)
    
    def insert(self, pointNode):
        self.heap.append(pointNode)
        parent = (self.size() - 2)//2
        while parent > 0:
            self.maxHeapify(parent)
            parent = (parent-1)//2
        self.maxHeapify(0)
        
    def top(self):
        return self.heap[0]
        
    def extractMax(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        maxElement = self.heap.pop()
        self.maxHeapify(0)
        return maxElement
    
    def maxHeapify(self, index):
        largest = index
        leftChild = 2*index + 1
        rightChild = 2*index + 2
        if leftChild < self.size() and self.heap[leftChild].distance > self.heap[largest].distance:
            largest = leftChild
        if rightChild < self.size() and self.heap[rightChild].distance > self.heap[largest].distance:
            largest = rightChild
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.maxHeapify(largest)

class Solution:
    
    def euclidean(self, x, y):
        return math.sqrt(x**2 + y**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = MaxHeap()
        for i in range(k):
            x, y = points[i]
            pointNode = Node(x, y, self.euclidean(x, y))
            maxHeap.insert(pointNode)
        for i in range(k, len(points)):
            x, y = points[i]
            dist = self.euclidean(x, y) 
            if dist < maxHeap.top().distance:
                maxHeap.extractMax()
                maxHeap.insert(Node(x, y, dist))
        return [element.point for element in maxHeap.heap]