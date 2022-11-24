# Recursive

# In-Order Traversal
# Left -> Self -> Right
class Node:
  def __init__(self, item):
    self.data = item
    self.left = None
    self.right = None
    
  def inorder(self):
    traversal = []
    if self.left:
      traversal += self.left.inorder()
    traversal.append(self.data)
    if self.right:
      traversal += self.right.inorder()
    return traversal
  
class BinaryTree:
  def __init__(self, r):
    self.root = r
  def inorder(self):
    if self.root:
      return self.root.inorder()
    else:
      return []

def solution(x):
    return 0
  

# Pre-Order Traversal
# Self -> Left -> Right
class Node:
  def __init__(self, item):
    self.data = item
    self.left = None
    self.right = None
    
  def preorder(self):
    traversal = []
    traversal.append(self.data)
    if self.left:
      traversal += self.left.preorder()
    if self.right:
      traversal += self.right.preorder()
    return traversal
  
class BinaryTree:
  def __init__(self, r):
    self.root = r
  def preorder(self):
    if self.root:
      return self.root.preorder()
    else:
      return []

def solution(x):
    return 0
  
  
# Post-Order Traversal
# Left -> Right -> Self
class Node:
  def __init__(self, item):
    self.data = item
    self.left = None
    self.right = None
    
  def postorder(self):
    traversal = []
    if self.left:
      traversal += self.left.postorder()
    if self.right:
      traversal += self.right.postorder()
    traversal.append(self.data)
    return traversal
  
class BinaryTree:
  def __init__(self, r):
    self.root = r
  def postorder(self):
    if self.root:
      return self.root.postorder()
    else:
      return []

def solution(x):
    return 0
