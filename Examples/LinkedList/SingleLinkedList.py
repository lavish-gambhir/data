# Shivam Goyal 16-3-19

class Node(object):
    def __init__(self, data=None, nexval=None):
        self.data = data
        self.nexval = nexval


class SLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, node_data):
        new_node = Node(data=node_data)
        if self.head is None:
            self.head = new_node
        else:
            num = int(input("Insert at Beg Press-1, Insert at Mid Press-2, Insert at End Press-3 : "))
            if num == 1:
                self.insert_at_beg(new_node)
            elif num == 2:
                val = int(input("Enter value to insert node before it : "))
                self.insert_at_mid(new_node, val)
            elif num == 3:
                self.insert_at_end(new_node)
            else:
                print("Wrong Input")
                assert False

    def insert_at_beg(self, new_node):
        temp = self.head
        self.head = new_node
        new_node.nexval = temp

    def insert_at_mid(self, new_node, val):
        current_node = self.head
        prev_node = None
        flag, count = 0, 0
        while current_node is not None:
            count += 1
            if current_node.data == val:
                flag = 1
                break
            else:
                prev_node = current_node
                current_node = current_node.nexval
        if flag == 1:
            if count == 1:
                self.insert_at_beg(new_node)
            else:
                prev_node.nexval = new_node
                new_node.nexval = current_node
        else:
            assert False,"No Matching Found"

    def insert_at_end(self, new_node):
        current_node = self.head
        while current_node.nexval is not None:
            current_node = current_node.nexval
        current_node.nexval = new_node

    def traversing(self):
        current_node = self.head
        while current_node is not None:
            print("Value is :",current_node.data)
            current_node = current_node.nexval

    def delete_elem(self):
        current_node = self.head
        prev_node,count,flag=0,0,0
        comp_val = int(input("Enter Element you want to delete: "))
        while current_node is not None:
            count+=1
            if current_node.data == comp_val:
                flag=1
                break
            else:
                prev_node = current_node
                current_node = current_node.nexval

        if flag==1:
            if count == 1:
                self.head = current_node.nexval
            else:
                prev_node.nexval = current_node.nexval
        else:
            assert False,"No element Found to Delete"



h = SLinkedList()
num = int(input("Enter Number of Elemnets:"))
for i in range(num):
    print("Enter",i+1,"Element: ")
    h.append(int(input()))
h.traversing()
query = input("Want to perform delete Operation Y/N : ").lower()[0]
if query == 'y':
    h.delete_elem()
h.traversing()