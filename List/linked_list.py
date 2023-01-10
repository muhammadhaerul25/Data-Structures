class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class LinkedList: 
    def display(self,head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self,head,data): 
        if head is None:
            head = Node(data)
        else:
            current = head
            while current.next:
                current = current.next
            current.next = Node(data)
        return head
    
    def delete(self,head,position):
        if position == 0:
            head = head.next
        else:
            current = head
            for i in range(position-1):
                current = current.next
            current.next = current.next.next
        return head
    
    def reverse(self,head):
        if head is None:
            return None
        else:
            current = head
            prev = None
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
    

