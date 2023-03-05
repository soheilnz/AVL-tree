# AVL Tree:
#   {An AVL tree is self_balancing Binary search Tree (BST) where
# the difference between heights of left and right subtrees cannot
# be more than one for all nodes.}
# making AVL Tree:
# { rebalancing is done to restore AVL property and this process
# is called ROTATION.}

from queue_using_linkedlist import Queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)


def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)


def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftChild)
    postOrder(rootNode.rightChild)
    print(rootNode.data)


def levelOrder(rootNode):
    if not rootNode:
        return
    customQ = Queue()
    customQ.enQueue(rootNode)
    while not customQ.isEmpty():
        root = customQ.deQueue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQ.enQueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQ.enQueue(root.value.rightChild)


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("found")
    elif nodeValue < rootNode:
        if rootNode.leftChild.data == nodeValue:
            return "found"
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            return "found"
        else:
            searchNode(rootNode.rightChild, nodeValue)


# Insertion a node in AVL tree has 2 conditions:
# 1- rotation needed.(When the binary tree becomes dis balanced.
# 2- rotation is not required.


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotation(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


def leftRotation(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        rootNode = AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        #       LEFT, LEFT ROTATION
        return rightRotation(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    #       RIGHT, RIGHT ROTATION
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        leftRotation(rootNode)
    return rootNode


# {Time : O(log N)
# Space : O(log n)


def getMinV(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinV(rootNode.leftChild)


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)

    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = getMinV(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
        rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotation(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
        
    return rootNode

# Time: O(log N)
# space: o(log N)


def deleteEntire(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Success"


# Time: O(1)
# Space: O(1)

newAvl = AVLNode(5)
newAvl = insertNode(newAvl, 10)
newAvl = insertNode(newAvl, 15)
newAvl = insertNode(newAvl, 20)
newAvl = deleteNode(newAvl, 15)
deleteEntire(newAvl)
levelOrder(newAvl)
