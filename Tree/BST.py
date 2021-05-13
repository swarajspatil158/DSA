class BST:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

	# Average: O(log(n)) time / O(1) space
	# worst: O(n) time / O(1) space
	# Insert input value in BST
	def insert(self,val):
		currentNode = self
		while True:
			if val < currentNode.val:
				if currentNode.left is None:
					currentNode.left = BST(val)                             
					break
				else:
					currentNode = currentNode.left
			
			elif val > currentNode.val:
				if currentNode.right is None:
					currentNode.right = BST(val)
					break
				else:
					currentNode = currentNode.right
		return self
	

	# Average: O(log(n)) time / O(1) space
	# worst: O(n) time / O(1) space
	# Search input value in BST
	def search(self,val):
		currentNode = self
		while currentNode != None:
			if val < currentNode.val:
				currentNode = currentNode.left
			elif val > currentNode.right:
				currentNode = currentNode.right
			else:
				return val == currentNode.val
		return False

	# def remove(self, val, parentNode = None):
	# 	currentNode = self
	# 	while currentNode:
	# 		if val < currentNode.val:
	# 			parentNode = currentNode
	# 			currentNode = currentNode.left
	# 		elif val > currentNode.val:
	# 			parentNode = currentNode
	# 			currentNode = currentNode.right
	# 		else:
	# 			if currentNode.left != None and currentNode.right != None:
	# 				currentNode.val = currentNode.right.getMinVal()