
class BPNode:
    '''
    A B+ tree is an m-ary tree with a variable but often large number of children per node. 
    A B+ tree consists of a root, internal nodes and leaves.
    The root may be either a leaf or a node with two or more children.

    A B+ tree can be viewed as a B-tree in which each node contains only keys (not key-value pairs), 
    and to which an additional level is added at the bottom with linked leaves. 

    In computer science, a B-tree is a self-balancing tree data structure
    that maintains sorted data and allows searches,
    sequential access, insertions, and deletions in logarithmic time:
    1. Every node has at most m children.
    2. Every non-leaf node (except root) has at least ⌈m/2⌉ child nodes.
    3. The root has at least two children if it is not a leaf node.
    4. A non-leaf node with (k) children contains (k-1) keys.
    5. All leaves appear in the same level and carry no information.

    * there is a maximum number of (children nodes):M and a maximum number of (values):L of a node
    '''
    def __init__(self, m, l, e=[], isRoot=False):
        '''
        in a B+Tree the number of keys is the maximum number of leafs-1 (M-1)
        the first key is the first least element of the SECOND child node
        the second key is the first least elment of the THIRD child node
        and so on....
        '''
        self.m = m # the maximum number of child nodes
        self.l = l # the maximum number of elements
        
        self.children = [] # no children or just leafs?
        self.elements = e
        self.keys = []

        self.isRoot = isRoot
        self.isLeaf = False

        self.leftSibling = None
        self.rightSibling = None
        self.root = None

        self.insert(e)


    def insert(self, e):
        '''
        ## algo:
        1. we check to see if the number of child nodes is surpassed
        2. we check if the maximum number of elements is surpassed

        3. if true: 
            split the current node into two nodes
            (if the number of elements is odd then the rightSibling will have and odd number)
        4. see if leftSibling == None
            if true:
                if rightSibling == None
                    rightSibling = BPnode(...)
                else: rightSibling.insert(e) #recursively
            else:
                leftSibling.insert(e)

        ## we will insert only one element at a time for the sake of simplicity
        '''
        if (len(self.children) >= self.m) or (len(self.elements) >= self.l):
            self.split(e)
        elif e == []:# inesrt the value in children and update the root's keys if necessary
            pass
        else:    
            self.elements.append(e)# we need to organize this list after insertion
            if self.root:
                self.root.update_keys()


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
                if type(child) is BPNode:
                    child.delete(e)
        
    def split(self, e):
        '''
        splits the current node into two and updates the keys
        '''
        leftNode = BPNode(self.l, self.m, self.elements[:(self.m)//2])
        rightNode = BPNode(self.l, self.m, self.elements[(self.m)//2:])
        rootNode = BPNode(self.l, self.m)

        leftNode.rightSibling = rightNode
        rightNode.leftSibling = leftNode

        rightNode.insert(e)
        rootNode.keys.append(rightNode.elements[0])
        self.update_keys()

    def update_keys(self):
        '''
        updates the keys of the current node according to the children
        some times we need to updates the parent node of the parent node how?
        '''
        for i in range(len(self.children)-1):
            if self.children[i+1].isLeaf == True:
                self.keys[i] = self.children[i+1]
            else:
                print("todo XD") 

    def balance(self):
        '''
        there will be the same algorithm to be done in order to balance a BTree after
        each insertion/deletion therefore we will put it here and call it at the end
        of insert() and delet()
        this function could take in a BPnode object also in order to run a lesser number of steps
        to balance out the whole tree(takes a node child of a tree but in the end the whole tree is balanced)
        '''
        pass


    def __repr__(self):
        return "Node :{keys=[" + str(self.keys) + "] ; elements=[" + str(self.elements) + "]; children=["+str(self.children) +"]; "
        

    def __str__(self):
        return "Node :{keys=[" + str(self.keys) + "] ; elements=[" + str(self.elements) + "]; children=["+str(self.children) +"]; "

def test1():
    BPTree = BPNode(3, 4, [], True)
    BPTree.insert(20)
    BPTree.insert(18)
    BPTree.insert(22)
    BPTree.insert(28)
    print(BPTree)
    BPTree.insert(25)


def main():
    test1()

if __name__== "__main__":
    main()
        


    """
    ...
    repr
    iter
    next
    """

