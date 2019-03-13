class Node(object):
    def __init__(self, data=None, nextval=None):
        self.data = data
        self.nextval = nextval


class SLinked(object):
    def __init__(self, head=None):
        self.head = head

    def traversing(self):
        if self.head is None:
            print("No point to the Next element")
        else:
            current_node = self.head
            while current_node is not None:
                print("Value is :",current_node.data)
                current_node = current_node.nextval
            print("----------------------------------")

    def insertion_at_begin(self,node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            self.head= node
            node.nextval = temp

    def insertion_at_end(self,node):
        current_node = self.head
        if current_node is None:
            print("No Elements in the list")
        else:
            while current_node.nextval is not None:
                current_node = current_node.nextval
            current_node.nextval = node

    def insert_in_mid(self,ins_node,comp_node):
        current_node= self.head
        prev = None
        if current_node is None:
            print("List is Empty")
        while current_node.data != comp_node.data:
            prev = current_node
            current_node = current_node.nextval
        prev.nextval = ins_node
        ins_node.nextval = current_node



n1 = Node(1)
n2 = Node(3)
n3 = Node(5)
n4 = Node(0)
n5 = Node(7)
n6 = Node(4)

h = SLinked(n1)
n1.nextval = n2
n2.nextval = n3

h.traversing()
h.insertion_at_begin(n4)
h.traversing()
h.insertion_at_end(n5)
h.traversing()
h.insert_in_mid(n6,n3)
h.traversing()