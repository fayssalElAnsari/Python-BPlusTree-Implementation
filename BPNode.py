
# TODO: insert function
# TODO: find function
# TODO: delete function
# TODO: show tree functionS
# TODO: unit tests

'''
### ALL POSSIBLE SCENARIOS DESCRIPTIONS AND TESTS ###
[x] 1. insertion of non organized elements in the possible limit of L and M gives out an organized list 
[x] 2. no left sibling and no right sibling => 
    root leaf becomes root only,
    two children leafs are created, largest elements are inserted in the new leaf node
    if odd number of total elements => more elements in the right child than in the left
    root node key array contains the least element of the right node
[x] 3. insertion into a leaf non root node past the limit of L that has space in left sibling
    => left sibling takes the smallest element of the right child
    => the lowest value in the right child could change
        => key in parent node should change also
[x] 4. another similar insertion to fill out the left child and update the key of parent
[x] 5. insertion into a right child (leaf non root) that has no right sibling and a full left sibling
    => child node splits and a key is added to the parent node
[ ] 6. internal node (non leaf root) has too many children, has no left sibling and no right sibling
    => it splits
    => same rules that apply to leaf nodes apply to inner nodes
..
.
'''

class BPTree:
    def __init__(self, m, l):
        self.root = BPNode()
        self.m = m 
        self.l = l

    def find(self, e):
        '''
        pass in a number and see if it's already in the tree
        there must be an efficient way to look for an element without going through all the children nodes
        '''
        return self.root.find(e)

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
    def __init__(self, m, l):
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

        self.leftSibling = None
        self.rightSibling = None
        self.parent = None

    def isRoot(BPNode):
        if BPNode.parent == None:
            return True

    def isLeaf(BPNode):
        if len(BPNode.children) == 0:
            return True

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
        # if the current node is an inner node we should check the keys and the first element of each child node
        there will be three types of nodes:
        the first is a root (root and leaf root and not leaf)
        the second is a leaf 
        the third is an inner node meaning not leaf and not root
        '''
        if(not self.isLeaf()):
            find_res = self.find(new_element)
            if (not find_res[0]):
                find_res[1].insert(new_element)
        elif(self.isLeaf()):
            if(self.isRoot()):
                all_elements = self.elements.copy()
                all_elements.append(new_element)
                all_elements.sort(reverse=False)

                if (len(self.children) >= self.m) or (len(self.elements) >= self.l):
                    if(self.leftSibling == None):
                        if(self.rightSibling == None):
                            self.split(new_element)
                        else:
                            self.rightSibling.insert(all_elements[0]) #lowest value = all_elements[0]
                            self.elements = all_elements[1:].copy() # then put the remaining elements in self
                            self.parent.update_keys()
                    else:
                        self.leftSibling.insert(all_elements[0])
                        self.elements = all_elements[1:].copy()
                        self.parent.update_keys()
                else:    # inesrt the value in children and update the root's keys if necessary
                    self.elements.append(new_element)
                    self.elements.sort(reverse=False)
                    # print(self.elements)

                    # if self.parent:
                    #     self.parent.update_keys()
            else:
                if (len(self.children) >= self.m) or (len(self.elements) >= self.l):
                    if(self.leftSibling == None or len(self.leftSibling.elements) >= self.leftSibling.l):
                        if(self.rightSibling == None or len(self.rightSibling.elements) >= self.rightSibling.l):
                            self.split(new_element)
                        else:
                            self.rightSibling.elements.append(new_element)
                            self.rightSibling.elements.sort(reverse=False)
                            self.parent.update_keys()
                    else:
                        all_elements = self.elements.copy()
                        all_elements.append(new_element)
                        all_elements.sort(reverse=False)
                        self.leftSibling.insert(all_elements[0])
                        self.elements = all_elements[1:].copy()
                        self.parent.update_keys()
                else:    # inesrt the value in children and update the root's keys if necessary
                    self.elements.append(new_element)
                    self.elements.sort(reverse=False)

        else:
            '''
            if the current node is an inner node then we should compare the new_elment to the first key
            if the new element is less than the current key (first key) we should set the ....
            '''
            index = 0
            while(len(self.keys) >= index+1 and new_element >= self.keys[index]):
                index = index + 1
            self.children[index].insert(new_element)

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
        if (self.isRoot()):
            leftNode = BPNode(self.m, self.l)
            rightNode = BPNode(self.m, self.l)
            
            leftNode.parent = self
            rightNode.parent = self

            leftNode.rightSibling = rightNode
            rightNode.leftSibling = leftNode

            all_elements = self.elements.copy()
            all_elements.append(new_element)
            all_elements.sort(reverse=False)
            
            for element in (all_elements[:(self.l)//2]) :
                leftNode.insert(element)

            for element in (all_elements[(self.l)//2:]) :
                rightNode.insert(element)

            self.children.append(leftNode)
            self.children.append(rightNode)

            # turn into an inner node
            self.elements = []
            self.keys.append(rightNode.elements[0])

            self.update_keys()

            print(" >: " + str(leftNode))
            print(" >: " + str(rightNode))
        else:   
            if self.rightSibling == None:# the node to split (self) is not a root node
                # in this case instead of keeping this node as an inner node we will make it a left leaf node?

                rightNode = BPNode(self.m, self.l)
                
                rightNode.parent = self.parent

                self.rightSibling = rightNode
                rightNode.leftSibling = self

                all_elements = self.elements.copy()
                all_elements.append(new_element)
                all_elements.sort(reverse=False)

                self.elements = []
                self.parent.children.append(rightNode)
                
                for element in (all_elements[:(self.l)//2]) :
                    self.insert(element)

                for element in (all_elements[(self.l)//2:]) :
                    rightNode.insert(element)

                print(" >: " + str(self))
                print(" >: " + str(rightNode))
                self.parent.update_keys()
            else:
                self.parent.split(new_element)# TODO: final insertion scenario

    def find(self, e):
        '''
        pass in a number and see if it's already in the tree
        there must be an efficient way to look for an element without going through all the children nodes
        ordered!!
        '''
        if self.isLeaf():
            for element in self.elements:
                if element == e:
                    return (True, self)
            return (False, self)
        else:
            for key in self.keys:
                if (key == e):
                    return (True, self.children[self.keys.index(key) + 1].find(e)[1]) # fix?
                elif (key >= e):
                    return self.children[self.keys.index(key)].find(e)
            return self.children[len(self.children) - 1].find(e)
                    


    def delete(self, e):
        '''
        deletes an element from a B-Tree if already existant
        if the element doesn't exist print out that it's non existant
        and do nothing else.
        this function should probably use the previously defined function: find()
        '''
        print(" !! delete start")
        search_res = self.find(e)
        print(search_res)

        if search_res[0]:
            print(e)
            print(search_res[0])
            print(search_res[1])
            print(search_res[1].elements)
            search_res[1].elements.remove(e)
            search_res[1].parent.update_keys()
            return True
        else:
            return False

    def update_keys(self):
        '''
        updates the keys of the current node according to the children
        some times we need to updates the parent node of the parent node how?
        '''
        for i in range(len(self.children)-1):
            if self.children[i+1].isLeaf() == True:
                try:
                    self.keys[i] = self.children[i+1].elements[0]
                except IndexError:
                    self.keys.append(None)
                    self.keys[i] = self.children[i+1].elements[0]
                print("updating key:" + str(i) + " to:" + str(self.children[i+1].elements[0]))
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
        return "Node :{keys=" + str(self.keys) + " ; elements=" + str(self.elements) + "; children="+str(self.children) +"}"
        

    def __str__(self):
        return "Node :{keys=" + str(self.keys) + " ; elements=" + str(self.elements) + "; children="+str(self.children) +"}"

    def print_tree(self):
        # for child in self.children:
        #     child.print_tree()
        print(self)

def test_insert_1():
    BPTree = BPNode(3, 4)
    BPTree.insert(20)
    BPTree.insert(18)
    BPTree.insert(22)
    BPTree.insert(28)
    BPTree.print_tree()

    BPTree.insert(25) # 5 elements in a leaf node that can only contain (L=4) elements
    BPTree.insert(41)
    BPTree.insert(23)
    BPTree.print_tree()
    BPTree.insert(42)
    BPTree.print_tree()
    BPTree.insert(53) # left sibling is full, right is None => inner node splits => a key 41 is added to root
    BPTree.print_tree()

    BPTree.insert(32)
    BPTree.print_tree()
    BPTree.insert(33)
    BPTree.print_tree()
    BPTree.insert(38)
    BPTree.print_tree()

    # BPTree.insert(24) # root node should split (using the same mechanism as before)
    # BPTree.print_tree()
    return BPTree

def test_search_1():
    BPTree = test_insert_1()
    print(str(1) + " in " + str(BPTree.find(1))) # false
    print(str(25) + " in " + str(BPTree.find(25))) # true
    print(str(38) + " in " + str(BPTree.find(38))) # true
    print(str(18) + " in " + str(BPTree.find(18))) # true
    print(str(28) + " in " + str(BPTree.find(28))) # true
    print(str(32) + " in " + str(BPTree.find(32))) # true
    print(str(33) + " in " + str(BPTree.find(33))) # true
    print(str(38) + " in " + str(BPTree.find(38))) # true
    print(str(39) + " in " + str(BPTree.find(39))) # true
    print(str(41) + " in " + str(BPTree.find(41))) # true
    print(str(53) + " in " + str(BPTree.find(53))) # true
    print(str(54) + " in " + str(BPTree.find(54))) # true
    print(str(100) + " in " + str(BPTree.find(100))) # false

def test_delete_1():
    a_tree = test_insert_1()
    a_tree.delete(25) # deletes 25
    print(a_tree)
    a_tree.delete(18)
    print(a_tree)
    a_tree.delete(23)
    print(a_tree)
    a_tree.delete(38)
    print(a_tree)
    a_tree.delete(1002)
    print(a_tree)

def main():
    # test_insert_1()
    # test_search_1()
    test_delete_1()

if __name__== "__main__":
    main()
    """
    ...
    repr
    iter
    next
    """

