import math
class MinHeap:

	def __init__(self):
		self.heap = []

	def insert(self,x):
		self.heap.append(x)
		self._siftUp()
	
	def delete(self):
		minVal = self.heap[0]
		self.heap[0] = self.heap[-1]
		self.heap.pop()
		self._siftDown()
		return minVal

	def peek(self):
		return self.heap[0]

	def getSize(self):
		return len(self.heap)

	def clear(self):
		self.heap.clear()

	def _siftUp(self):
		curr_idx = len(self.heap) - 1
		parent_idx = math.ceil(curr_idx/2) - 1
		while parent_idx >= 0 and self.heap[curr_idx] < self.heap[parent_idx]:
			self.heap[curr_idx],self.heap[parent_idx] = self.heap[parent_idx],self.heap[curr_idx]
			curr_idx, parent_idx= parent_idx, math.ceil(parent_idx/2) - 1
	
	def _siftDown(self):
		parent_idx = 0
		heap_size = len(self.heap)
		child_idx = heap_size
		left_idx = 2*parent_idx + 1
		right_idx = 2*parent_idx + 2
		if right_idx < heap_size:
			child_idx = left_idx if self.heap[left_idx] < self.heap[right_idx] else right_idx
		elif left_idx < heap_size:
			child_idx = left_idx
		while child_idx < heap_size and self.heap[child_idx] < self.heap[parent_idx]:
			self.heap[child_idx],self.heap[parent_idx] = self.heap[parent_idx],self.heap[child_idx]
			parent_idx = child_idx
			child_idx = heap_size
			left_idx = 2*parent_idx + 1
			right_idx = 2*parent_idx + 2
			if right_idx < heap_size:
				child_idx = left_idx if self.heap[left_idx] < self.heap[right_idx] else right_idx
			elif left_idx < heap_size:
				child_idx = left_idx

	def printHeap(self):
		print(' '.join(map(str,self.heap)))


class MaxHeap:

	def __init__(self):
		self.heap = []

	def insert(self,x):
		self.heap.append(x)
		self._siftUp()
	
	def delete(self):
		minVal = self.heap[0]
		self.heap[0] = self.heap[-1]
		self.heap.pop()
		self._siftDown()
		return minVal

	def peek(self):
		return self.heap[0]

	def getSize(self):
		return len(self.heap)

	def clear(self):
		self.heap.clear()

	def _siftUp(self):
		curr_idx = len(self.heap) - 1
		parent_idx = math.ceil(curr_idx/2) - 1
		while parent_idx >= 0 and self.heap[curr_idx] > self.heap[parent_idx]:
			self.heap[curr_idx],self.heap[parent_idx] = self.heap[parent_idx],self.heap[curr_idx]
			curr_idx, parent_idx= parent_idx, math.ceil(parent_idx/2) - 1
	
	def _siftDown(self):
		parent_idx = 0
		heap_size = len(self.heap)
		child_idx = heap_size
		left_idx = 2*parent_idx + 1
		right_idx = 2*parent_idx + 2
		if right_idx < heap_size:
			child_idx = left_idx if self.heap[left_idx] > self.heap[right_idx] else right_idx
		elif left_idx < heap_size:
			child_idx = left_idx
		while child_idx < heap_size and self.heap[child_idx] > self.heap[parent_idx]:
			self.heap[child_idx],self.heap[parent_idx] = self.heap[parent_idx],self.heap[child_idx]
			parent_idx = child_idx
			child_idx = heap_size
			left_idx = 2*parent_idx + 1
			right_idx = 2*parent_idx + 2
			if right_idx < heap_size:
				child_idx = left_idx if self.heap[left_idx] > self.heap[right_idx] else right_idx
			elif left_idx < heap_size:
				child_idx = left_idx

	def printHeap(self):
		print(' '.join(map(str,self.heap)))


class MedianHeap:

	def __init__(self):
		self.minHeap = MinHeap()
		self.maxHeap = MaxHeap()

	def insert(self,x):
		if self.maxHeap.getSize() == 0:
			self.maxHeap.insert(x)
		elif x > self.maxHeap.peek():
			self.minHeap.insert(x)
		else:
			self.maxHeap.insert(x)
		if self.maxHeap.getSize() - self.minHeap.getSize() > 1:
			self.minHeap.insert(self.maxHeap.delete())
		elif self.minHeap.getSize() - self.maxHeap.getSize() >= 1:
			self.maxHeap.insert(self.minHeap.delete())
	def getMedian(self):
		if self.maxHeap.getSize() == self.minHeap.getSize():
			return (self.maxHeap.peek()+self.minHeap.peek())/2
		else:
			return self.maxHeap.peek()
	def clear(self):
		self.minHeap.clear()
		self.maxHeap.clear()

