
class BNode:
    '''
    In computer science, a B-tree is a self-balancing tree data structure
    that maintains sorted data and allows searches,
    sequential access, insertions, and deletions in logarithmic time:
    1. Every node has at most m children.
    2. Every non-leaf node (except root) has at least ⌈m/2⌉ child nodes.
    3. The root has at least two children if it is not a leaf node.
    4. A non-leaf node with (k) children contains (k-1) keys.
    5. All leaves appear in the same level and carry no information.

    * children and elements is the same list therfore a child can be either a node or just a value
    '''
    def __init__(self, m, elements=None, isRoot=False):
        '''
        m is the maximum number of elements of this node
        e is only one number (element) to initialise the tree with?
        e can be more than one number because of the condition:
            =>     Every non-leaf node (except root) has at least ⌈m/2⌉ child nodes.

        * what happens if we pass in only one element to the e param when we have l>1?
            the root node is created nevertheless
            and the l param is no longer a param but is calculated with l = m/2

        '''
        self.m = m
        self.children = [] # no children or just leafs?
        self.isRoot = isRoot
        self.isLeaf = False
        # if e is jut one element, meaning we could be in the case of the root node
        # then we should set the elements with [e]
        # elif it's already a list we set it with e directly
        self.insert(e)



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

    * should we pass in many elements or just one at a time??
    '''
    if type(e) is list:
        # more than one element has been passed to e
        # we should check for max before setting the elements values
        # we might use the insrt() function later but for now we will check manually
        if len(e) <= l:
            self.children = elements
        else: 
            print("/!\ The number of elements passed is bigger than Max")
            for e in range(len(elements)):
                if e<m:
                    self.children.append(elements[e])
                else:
                    #create a new node and insert the remaining elements into it
                    child = BNode(self.m, elements[m:]) # the elements are the remaining elements of node (and are inserted automatically)
                    self.children.append(child) # the new child is added to the list of children of this node


    elif e == None:
        self.elements = []
        self.isLeaf = True
    else:
        self.elements = elements #only one element

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
    if e in self.children:
        self.children.remove(e)
    else:
        for child in children:
            if type(child) is BNode:
                child.delete(e)
    
"""
...
repr
iter
next
"""

