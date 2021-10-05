class BinaryTreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left = None
        self.right = None

def printTree(root):
    if root == None:
        return
    else:
        print(root.data)
        printTree(root.left)
        printTree(root.right)
    
def printTreeDetailed(root):
    if root == None:
        return
    else:
        print(f"{root.data} : ",end="")
        if root.left != None:
            print(f"{root.left.data}",end = "")
        if root.right != None:
            print(f", {root.right.data}",end="")
        print("")
        printTreeDetailed(root.left)
        printTreeDetailed(root.right)
def NoOfNodes(root):
    if root == None:
        return 0
    else:
        left_count=NoOfNodes(root.left)
        right_count=NoOfNodes(root.right)
    return 1 + left_count + right_count
root = BinaryTreeNode(1)
node_1 = BinaryTreeNode(2)
node_2 = BinaryTreeNode(3)
node_3 = BinaryTreeNode(4)
node_4 = BinaryTreeNode(5)
node_5 = BinaryTreeNode(6)
node_6 = BinaryTreeNode(7)

root.left = node_1
root.right = node_2
node_1.left = node_3
node_1.right = node_4
node_2.left = node_5
node_2.right = node_6

# ----------------------

printTreeDetailed(root)
print(NoOfNodes(root))



