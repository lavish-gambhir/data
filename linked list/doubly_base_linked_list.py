# Doubly linked list abstraction

class _DoubleLinkedBase(object):
    """A base class providing a doubly linked list representation."""

    class _Node(object):
        __slots__ = 'element', 'prev_node', 'next_node'

        def __init__(self, element, prev_node, next_node):
            self.element = element
            self.prev_node = prev_node
            self.next_node = next_node

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.next_node = self._trailer
        self._trailer.prev_node = self._header
        self._size = 0


    def __len__(self):
        """Return the number of elements in the list."""
        return self._size


    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0


    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        temp = self._Node(e, predecessor, successor)
        predecessor.next_node = temp
        successor.prev_node = temp
        self._size += 1
        return temp


    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node.prev_node
        successor = node.next_node
        predecessor.next_node = successor
        successor.prev_node = predecessor
        self._size -= 1
        element = node.element
        node.prev_node = node.next_node = node.element
        return element
