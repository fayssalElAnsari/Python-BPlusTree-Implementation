
class Node:
    '''
    In computer science, a B-tree is a self-balancing tree data structure
    that maintains sorted data and allows searches,
    sequential access, insertions, and deletions in logarithmic time:
    1. Every node has at most m children.
    2. Every non-leaf node (except root) has at least ⌈m/2⌉ child nodes.
    3. The root has at least two children if it is not a leaf node.
    4. A non-leaf node with (k) children contains (k-1) keys.
    5. All leaves appear in the same level and carry no information.
    '''
    def __init__(self, l, u, e, isRoot=False):
        '''
        l is the 
        '''
        self.children = []
        self.elements = [e]
        self.isRoot = isRoot
        


def __init__(self, l, u):
    self.elements = []
    self.children = []
    self.L = l
    self.U = u
    self.isLeaf = False



def insert(self, e):
    '''
    inserts an element into the B-Tree according to the B-Tree rules:
    1. Every node has at most m children => check the number of children before inserting 
    2. Every non-leaf node (except root) has at least ⌈m/2⌉ child nodes => 
            => If we need to make a new node then we should migrate some values from the current node in order to have m/2 in the new child node
    3. The root has at least two children if it is not a leaf node 
            =>  If the current node is a root node (we should define a bool isRoot variable), 
                and we need to create a new node we should make also another child node
    4.... don't know about these

    '''
    self.elements.append(e)

def find(self, e):
    '''
    pass in a number and see if it's already in the tree
    there must be an efficient way to look for an element without going through all the children nodes
    '''
    pass

def delete(self, e):
    '''
    deletes an element from a B-Tree if already existant
    if the element doesn't exist print out that it's non existant
    and do nothing else.
    this function should probably use the previously defined function: find()
    '''
    self.elements.remove(e)


    
"""
...
repr
iter
next
"""

