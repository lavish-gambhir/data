# Binary Tree implementation

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


if __name__ == '__main__':
	root =Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)