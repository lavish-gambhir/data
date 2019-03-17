# Shivam Goyal 17-03-19

class Node():
    def __init__(self, preval=None, data=None, nexval=None):
        self.data = data
        self.preval = preval
        self.nexval = nexval


class SLinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, node_data):
        new_node = Node(data=node_data)
        if self.head is None:
            self.head = new_node
        else:
            num = int(input("insert at first - Press 1 ,insert at last - Press 2,insert in mid - Press 3 :"))
            if num == 1:
                self.insert_at_begin(new_node)
            elif num == 2:
                self.insert_at_end(new_node)
            elif num == 3:
                val = int(input("Enter value to insert node before it :"))
                self.search_and_insert(new_node, val)
            else:
                assert False,"Wrong Input"

    def insert_at_begin(self, node_data):
        temp = self.head
        self.head = node_data
        self.head.nexval = temp
        temp.preval = self.head

    def search_and_insert(self,node_data,value):
        current_node= self.head
        flag = 0
        count = 0
        while current_node is not None:
            count += 1
            if current_node.data == value:
                flag = 1
                break
            else:
                current_node = current_node.nexval
        if flag == 1:
            if count==1:
                self.insert_at_begin(node_data)
            else:
                prev_node = current_node.preval
                prev_node.nexval = node_data
                node_data.preval = prev_node
                node_data.nexval = current_node
                current_node.preval = node_data
        else:
            assert False,"No Matching Found"

    def delete_element(self):
        current_node = self.head
        count,flag = 0,0
        num = int(input("Enter element you want to delete : "))

        while current_node is not None:
            count+=1
            if current_node.data == num:
                flag=1
                break
            else:
                current_node = current_node.nexval
        if flag==1:
            if count==1:
                temp = current_node.nexval
                temp.preval = None
                self.head = temp
            else:
                prev_node = current_node.preval
                next_node = current_node.nexval
                prev_node.nexval = next_node
                next_node.preval = prev_node



    def insert_at_end(self, node_data):
        current_node = self.head
        while current_node.nexval is not None:
            current_node = current_node.nexval
        current_node.nexval = node_data
        node_data.preval = current_node

    def traversing_forward(self):
        if self.head is None:
            print("Linked List Empty")
        else:
            current_node = self.head
            while current_node is not None:
                print("Value is :", current_node.data)
                current_node = current_node.nexval
            print("--------------------------------------------")

    def traversing_backward(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            current_head = self.head
            while current_head.nexval is not None:
                current_head = current_head.nexval
            while current_head is not None:
                print("Reverse value is :",current_head.data)
                current_head = current_head.preval
            print("--------------------------------------------")


h = SLinkedList()
num = int(input("Enter number of elements you want to insert: "))
for i in range(num):
    print("Enter",i+1,"Element: ")
    ele = int(input())
    h.append(ele)
h.traversing_forward()
h.traversing_backward()

print("Want to Perform delete operation Y/N? :")
query = input().lower()[0]
if query == 'y':
    h.delete_element()
    h.traversing_forward()
    h.traversing_backward()