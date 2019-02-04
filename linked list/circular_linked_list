# Round robin

from empty import Empty


class CircularQueue(object):
    """Queue implementation using a circularly linked list for storage."""

    class _Node(object):
        __slots__ = 'element', 'next_node'

        def __init__(self, element, next_node):
            self.element = element
            self.next_node = next_node


    def __init__(self):
        """Create an empty queue."""
        self._tail = None
        self._size = 0


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
        head = self._tail.next_node
        return head.element


    def dequeue(self):
        """Remove and return the first element of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty!')
        oldhead = self._tail.next_node
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next_node = oldhead.next_node
        self._size -= 1
        return oldhead.element


    def enqueue(self, item):
        """Add an element to the back of the queue."""
        temp = self._Node(item, None)
        if self.is_empty():
            temp.next_node = temp
        else:
            temp.next_node = self._tail.next_node
            self._tail.next_node = temp
        self._tail = temp
        self._size += 1


    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail.next_node
