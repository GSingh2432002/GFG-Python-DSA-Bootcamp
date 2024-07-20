# Middle of Linked List
class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
    print()


    
def printMiddle(ptr):
    if head == None:
        return
    slow = head
    fast = head
    while fast!= None and fast.next!=None :
        slow=slow.next
        fast=fast.next.next
        
    print(slow.data)
    
            
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
printMiddle(head)