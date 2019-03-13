# Deque using Doubly linked list

from doubly_base_linked_list import _DoubleLinkedBase
from empty import Empty


class LinkedDeque(_DoubleLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._header.next_node.element


    def last(self):
        """Return (not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._trailer.prev_node.element


    def insert_first(self, e):
        """Add an element e to the front of the deque."""
        self._insert_between(e, self._header, self._header.next_node)


    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer.prev_node, self._trailer)


    def delete_first(self):
        """Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._delete_node(self._header.next_node)


    def delete_last(self):
        """Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._delete_node(self._trailer.prev_node)

