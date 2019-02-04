# Queue using Singly linked list.

from empty import Empty


class LinkedQueue(object):
    """FIFO queue implementation using a singly linked list for storage."""

    # ---------- _Node class ---------
    class _Node(object):
        __slots__ = 'element', 'next_node'

        def __init__(self, element, next_node):
            self.element = element
            self.next_node = next_node

    # ---------------------------------


    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size


    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0


    def first(self):
        """Return (not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty!')
        return self._head.element


    def dequeue(self):
        """Remove and return the first element of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty!')
        answer = self._head.element
        self._head = self._head.next_node
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer


    def enqueue(self, item):
        """Add an element to the back of the queue."""
        newest = self._Node(item, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail.next_node = newest
        self._tail = newest
        self._size += 1












