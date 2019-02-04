# Stack using Linked List

from empty import Empty

class LinkedStack(object):
    """LIFO Stack implementation using a singly linked list for storage."""

    # -------- _Node class --------
    class _Node(object):
        __slots__ = 'element', 'next_node'

        def __init__(self, element, next_node):
            self.element = element
            self.next_node = next_node

    # -----------------------------

    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0


    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size


    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0


    def push(self, item):
        """Add item to the top of the stack."""
        self._head = self._Node(item, self._head)
        self._size += 1


    def top(self):
        """Return (not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._head.element


    def pop(self):
        """Remove and return the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty!')
        answer = self._head.element
        self._head = self._head.next_node
        self._size -= 1
        return answer


