class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        last_node=self.head
        while(last_node.next):
            last_node=last_node.next

        last_node.next=new_node

    def print_list(self):
        cur_node=self.head
        while(cur_node):
            print(cur_node.data)
            cur_node=cur_node.next

    def prepend(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node

    def insert_after(self,prev_node,data):
        if(not prev_node):
            print("The node does not exist")
            return
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def del_node(self,key):
        cur_node=self.head
        if(cur_node and cur_node.data==key):
            self.head=cur_node.next
            cur_node=None
            return
        prev=None
        while(cur_node and cur_node.data!=key):
            prev=cur_node
            cur_node=cur_node.next

        if (cur_node is None):
            return

        prev.next=cur_node.next
        cur_node=None

    def del_by_pos(self,pos):
        cur_node=self.head
        if(pos==0):
            self.head=cur_node.next
            cur_node=None
            return
        count=1
        prev_node=None
        while(cur_node and count!=pos):
            prev_node=cur_node
            cur_node=cur_node.next
            count+=1

        if(cur_node is None):
            return

        prev_node.next=cur_node.next
        cur_node=None

    def len_iterative(self):
        cur_node=self.head
        count=0
        while(cur_node):
            count+=1
            cur_node=cur_node.next
        return count

    def len_recursive(self,node):
        if node is None:
            return 0
        return 1+self.len_recursive(node.next)
    
    def swap_nodes(self,key1,key2):
        if(key1==key2):
            return
        prev_1=None
        cur_1=self.head
        while(cur_1 and cur_1.data!=key1):
            prev_1=cur_1
            cur_1=cur_1.next

        prev_2=None
        cur_2=self.head
        while(cur_2 and cur_2.data!=key2):
            prev_2=cur_2
            cur_2=cur_2.next

        if(not cur_1 or not cur_2):
            return
        if (prev_1):
            prev_1.next=cur_2
        else:
            self.head=cur_2

        if(prev_2):
            prev_2.next=cur_1
        else:
            self.head=cur_1

        cur_1.next,cur_2.next=cur_2.next,cur_1.next

print("---append---")
list=LinkedList()
list.append(1)
list.append("a")
list.append("b")
list.append("c")
list.append("d")
list.print_list()
print("the length is ",list.len_iterative())
print("---prepend---")
list.prepend(5)
list.print_list()
print("the length is ",list.len_iterative())
print("---insert after---")
list.insert_after(list.head.next.next.next,"f")
list.print_list()
print("the length is",list.len_recursive(list.head))
print("---del with key---")
list.del_node(1)
list.print_list()
print("the length is ",list.len_iterative())
print("---delete with position---")
list.del_by_pos(3)
list.print_list()
print("the length is ",list.len_iterative())
print("---node_swap---")
list.swap_nodes("a","c")
list.print_list() 
        
