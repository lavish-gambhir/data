# Qeueue ADT

from empty import Empty


class ArrayQueue(object):
	"""FIFO queue implementation using a Python list as underlying storage."""
	DEFAULT_CAPACITY = 10 

	def __init__(self):
		"""Create an empty queue."""
		self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0


	def __len__(self):
		"""Return the number of elements in the queue."""
		return self._size


	def is_empty(self):
		"""Return True if the queue is empty."""
		return self._size == 0


	def first(self):
		"""Return (not remove) the element at the front of the queue.
		Raise Empty exception if the queue is empty.
		"""
		if self.is_empty():
			raise Empty('Queue is empty!')
		return self._data[self._front]


	def dequeue(self):
		"""Remove and return the first element of the queue.
		Raise Empty exception if the queue is empty.
		"""
		if self.is_empty():
			raise Empty('Queue is empty!')
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)
		self._size -= 1
		if 0 < self._size < len(self._data) // 4: # Shrinking the underlying array
			self._resize(len(self._data) // 2)
		return answer


	def enqueue(self, item):
		"""Add an element to the back of the queue."""
		if self._size == len(self._data):
			self._resize(2 * len(self._data))
		avail = (self._front + self._size) % len(self._data)
		self._data[avail] = item
		self._size += 1


	def _resize(self, cap):
		"""Resize to a new list of cap >= len(self)."""
		old = self._data
		self._data = [None] * cap
		walk = self._front
		for i in range(self._size):
			self._data[i] = old[walk]
			walk = (walk + 1) % len(old)
		self._front = 0


if __name__ == '__main__':
	q = ArrayQueue()
	print(q.first())



























