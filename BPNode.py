
# TODO: insert function
# TODO: find function
# TODO: delete function
# TODO: show tree functionS
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
    def __init__(self, m, l, isRoot=False):
        '''
        in a B+Tree the number of keys is the maximum number of leafs-1 (M-1)
        the first key is the first least element of the SECOND child node
        the second key is the first least elment of the THIRD child node
        and so on....
        '''
        self.m = m # the maximum number of child nodes
        self.l = l # the maximum number of elements
        
        self.children = [] # no children or just leafs?
        self.elements = []
        self.keys = []

        self.isRoot = isRoot # by default not a root
        self.isLeaf = True #every leaf is a leaf node at creation

        self.leftSibling = None
        self.rightSibling = None
        self.parent = None

    def insert(self, new_element):
        '''
        ## algo:
        1. we check to see if the number of child nodes is surpassed
        2. we check if the maximum number of elements is surpassed

        3. if true: 
            split the current node into two nodes
            (if the number of elements is odd then the rightSibling will have an odd number)
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
            if(self.leftSibling == None):
                if(self.rightSibling == None):
                    self.split(new_element)
            #     else: self.rightSibling.insert(e)
            # else: self.leftSibling.insert(e)
        else:    # inesrt the value in children and update the root's keys if necessary
            self.elements.append(new_element)
            self.elements.sort(reverse=False)
            # print(self.elements)

            # if self.parent:
            #     self.parent.update_keys()

    def split(self, new_element):
        '''
        splits the current node into two and updates the keys
        THIS node will become a left sibling or stay the root node of this tree?? 
            > will choose stay root
        how to go from the root node to the children???
            > using the keys?
        when splitting there are two cases:
            1. if the root to split is the root node it will stay the root node
            2. if not the root node it will become the left node 
        '''
        print("splitting...")
        leftNode = BPNode(self.m, self.l)
        rightNode = BPNode(self.m, self.l)
        
        leftNode.parent = self
        rightNode.parent = self

        leftNode.rightSibling = rightNode
        rightNode.leftSibling = leftNode
        
        for element in (self.elements[:(self.l)//2]) :
            leftNode.insert(element)
            print("inserting: " + str(element))
            print(leftNode)

        for element in (self.elements[(self.l)//2:]) :
            rightNode.insert(element)
            print("inserting: " + str(element))
            print(rightNode)

        rightNode.insert(new_element)

        self.children.append(leftNode)
        self.children.append(rightNode)

        print(leftNode)
        print(rightNode)

        # turn into an inner node
        self.isLeaf = False
        self.elements = []
        self.keys.append(rightNode.elements[0])

        # self.update_keys()


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
        return "Node :{keys=" + str(self.keys) + " ; elements=" + str(self.elements) + "; children="+str(self.children) +"; }"
        

    def __str__(self):
        return "Node :{keys=" + str(self.keys) + " ; elements=" + str(self.elements) + "; children="+str(self.children) +"; }"

    def print_tree(self):
        # for child in self.children:
        #     child.print_tree()
        print(self)

def test1():
    BPTree = BPNode(3, 4, True)
    BPTree.insert(20)
    BPTree.insert(18)
    BPTree.insert(22)
    BPTree.insert(28)
    BPTree.print_tree()

    BPTree.insert(25) # 5 elements in a leaf node that can only contain (L=4) elements
    # BPTree.insert(41)
    # BPTree.insert(23)
    BPTree.print_tree()


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

