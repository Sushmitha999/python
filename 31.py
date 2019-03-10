class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def BT(root): 
	if root is None: 
		return True
	queue = [] 
	flag = False
	queue.append(root) 
	while(len(queue) > 0): 
		tempNode = queue.pop(0) 
		if (tempNode.left): 
			if flag == True : 
				return False
			queue.append(tempNode.left) 
		else: 
			flag = True
		if(tempNode.right): 
			if flag == True: 
				return False
			queue.append(tempNode.right) 
		else: 
			flag = True
	return True
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(6) 

if (BT(root)): 
	print("complete Binary Tree")
else: 
	print("not a complete Binary Tree")
