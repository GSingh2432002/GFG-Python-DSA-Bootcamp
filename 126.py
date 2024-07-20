# Nth Node From end of Linked List
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printNthFromLast(self, N):
		main_ptr = self.head
		ref_ptr = self.head

		count = 0
		if(self.head is not None):
			while(count < N):
				if(ref_ptr is None):
					print("% d is greater than the no. pf nodes in list" % (N))
					return
				ref_ptr = ref_ptr.next
				count += 1

		if(ref_ptr is None):
			self.head = self.head.next
			if(self.head is not None):
				print("Node no. % d from last is % d "
					% (N, main_ptr.data))
		else:

			while(ref_ptr is not None):
				main_ptr = main_ptr.next
				ref_ptr = ref_ptr.next

			print("Node no. % d from last is % d "
				% (N, main_ptr.data))


# Driver's code
if __name__ == '__main__':
	llist = LinkedList()
	llist.push(20)
	llist.push(4)
	llist.push(15)
	llist.push(35)

	# Function call
	llist.printNthFromLast(4)