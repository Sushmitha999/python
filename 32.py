class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None

def insertLevelOrder(arr, root, i, n): 
	if i < n: 
		temp = newNode(arr[i]) 
		root = temp 
		root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n) 
		root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
	return root
def inOrder(root): 
	if root != None: 
		inOrder(root.left) 
		print(root.data,end=" ") 
		inOrder(root.right) 

if __name__ == '__main__': 
	arr = [1,2,3,6,4,8,9,10]
	n = len(arr) 
	root = None
	root = insertLevelOrder(arr, root, 0, n) 
	inOrder(root) 
	
