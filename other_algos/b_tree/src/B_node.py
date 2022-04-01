class B_node:
    def main():
        print("B_node")


    def __init__(self, parent, tree=None):
        '''
        Initializes a B_node instance

        This function will make a B_node object that has a 
        parent the parent passed in in argument

        Parameters
        ----------
        parent : B_node or Btree
            The parent of the current tree

        Returns
        -------
            An instance of the B_node class
        '''
        self.parent = parent
        if tree == None:
            self.tree = parent.tree
        else:
            self.tree = tree           
        self.keys = []
        self.children = []
        self.m = tree.m
        self.l = tree.l

        

    def search_element(self, element):
        '''
        Search for an element in the tree

        This function will check if an element exists in a given tree.
        The way it works is by calling itself recursively on the current node.
        starting from the current node it will check the keys for the existence
        of the element, if it exists it will return true. If not it will check if
        the current node is a leaf. If it's a leaf and there element is not in the
        keys then element doesn't exist in the current search. If it's not a leaf
        it will search all the children of the current node and therefore their 
        children recursively.

        Parameters
        ----------
        element : int
            The element to be checked if it exists in the current B_tree

        Returns
        -------
            true: if the element exists in the current search
            false: if the element doesn't exist in the search
        '''
        if element in self.keys:
            return True
        else:
            if self.is_leaf():
                return False
            else:
                for i in range(len(self.keys) - 1):
                    if element < self.keys[i]:
                        return self.children[i].search_element(element)
                        break
                return self.children[-1].search_element(element)
        

    def search_node(self, element):
        '''
        Search for a node containing the element in this node

        This function will check if an element exists in this node.
        The way it works is by calling itself recursively on the current node.
        starting from the current node it will check the keys for the existance
        of the element, if it exists it will return the node. If not it will 
        check if the current node is a leaf. If it's a leaf and the element 
        is not in the keys then element doesn't exist in the current search. 
        If it's not a leaf it will search all the children of the current 
        node and therefore their children recursively.

        Parameters
        ----------
        element : int
            The element to be checked if it exists in the current B_tree

        Returns
        -------
            B_node: the node in which this current element is or should be
        '''
        if self.is_leaf():
            return self
        else:
            for i in range(len(self.keys)):
                if element < self.keys[i]:
                    return self.children[i].search_node(element)
                    break
            return self.children[-1].search_node(element)


    def insert(self, element):
        '''
        Inserts an element in this node

        This function will insert an element in the current node.
        it can take in either a list of elements or an element.
        if the current node is a leaf it will use another function to insert
        the key directly into the list of keys of the current node.
        else it will search the node for the element and call itself on the result

        Parameters
        ----------
        element : int
            The element to be inserted in the current B_node

        Returns
        -------
            None
        '''
        if type(element) == list:
            for e in element:
                self.insert(e)
        else:
            if self.is_leaf():
                self.insert_key(element)
            else:
                (self.search_node(element)).insert(element)  


    def insert_key(self, element):
        '''
        Inserts an element in this node

        This function will insert an element in the current leaf.
        It will copy the list of keys in a new variable and then
        append the new element on it. Since the keys should be ordered
        the all_keys list will be sorted in ascending order.
        If the length of all keys is less than the order meaning 
        the current leaf is not yet full we can just assign the all_keys
        variable to the keys of this leaf. If not then we need to split this leaf

        Parameters
        ----------
        element : int
            The element to be inserted in the current leaf's list of keys

        Returns
        -------
            None
        '''
        if (element not in self.keys):
            all_keys = self.keys.copy()
            all_keys.append(element)
            all_keys.sort(reverse=False)
            if len(all_keys) < self.m:
                self.keys = all_keys
            else:
                self.split(element)
        else:
            print(str(element) + " already in keys list")


    def delete(self, element):
        '''
        Inserts an element in this node

        This function will insert an element in the current node.
        it can take in either a list of elements or an element.
        if the current node is a leaf it will use another function to insert
        the key directly into the list of keys of the current node.
        else it will search the node for the element and call itself on the result

        Parameters
        ----------
        element : int
            The element to be inserted in the current B_node

        Returns
        -------
            None
        '''
        node = self.search_node(element)
        node.delete_key(element)
        if len(node.keys) < self.l:
            node.rotate_clockwise()
        self.balance()


    def delete_key(self, element):
        '''
        deletes a keys from the current node directly.

        This function will be called on a 

        Parameters
        ----------
        element : int
            The element to be deleted from the current B_node

        Returns
        -------
            None
        '''
        if (element in self.keys):
            self.keys.remove(element)
        else:
            print(str(element) + " not in keys list!")


    def balance(self):
        '''
        Balances the current node and its descendents

        This function will be called after each deletion operation in order 
        to balance the current node and it's descendents

        Parameters
        ----------
            None

        Returns
        -------
            None
        '''
        # if self.is_leaf():
        self.delete_empty_child()
        for child in self.children:
            child.balance()


    def delete_empty_child(self):
        '''
        Deletes every empty child this current node has
        
        This function is a part of the balancing procedure

        Parameters
        ----------
            None

        Returns
        -------
            None
        '''
        for child in self.children:
            if (child.keys == []):
                self.children.remove(child)

    
    def rotate_clockwise(self):
        '''
        Rotates the keys of the of current node and its parent 
        and left sibling clockwise
        
        This function will be used in deletion process in case...
        '''
        if self.parent:
            index = self.parent.children.index(self) - 1
            if index > 0:
                if (self.parent.self.parent.children[index].keys) > self.l + 1:
                    left_key = self.parent.children[index].keys[-1]
                    upper_key = self.parent.keys[index]
                    self.parent.children[index].delete(left_key)
                    self.parent.delete(upper_key)
                    self.parent.insert(left_key)
                    self.insert(upper_key)
                else:
                    self.rotate_counter_clockwise()


    def rotate_counter_clockwise(self):
        '''
        Rotates the keys of the of current node and its parent 
        and right sibling clockwise
        
        This function will be used in deletion process in case...
        '''
        if self.parent:
            index = self.parent.children.index(self) + 1
            if index < len(self.parent.children):
                if (self.parent.self.parent.children[index].keys) > self.l + 1:
                    right_key = self.parent.children[index].keys[-1]
                    upper_key = self.parent.keys[index]
                    self.parent.children[index].delete(left_key)
                    self.parent.delete(upper_key)
                    self.parent.insert(right_key)
                    self.insert(upper_key)
                else:
                    self.merge()


    def merge(self):
        pass


    def split(self, element):
        '''
        Split the current node in two

        This function will take in an element and split the current node
        in two. The first step is to copy all the keys into a new variable
        then split them in half and then do the same for the children also
        the median key will be given to the parent. And the parent of the 
        children will be updated. A sibling node containing the right part of 
        the split is created.
        If the current node is not the root then list of children of the parent
        should be updated by taking in the sibling node directly after the current
        node. And the key is inserted in the parent as stated earlier. In this
        implementation the node to be split is traversed. There is another way
        to insert an element without having to traverse the nodes to be split
        by checking if the node is full and therefore traversing the tree only 
        one time.

        Parameters
        ----------
        element : int
            The element that will be added and caused the split

        Returns
        -------
            None
        '''
        all_keys = self.keys.copy()
        all_keys.append(element)
        all_keys.sort(reverse=False)
        median_index = len(all_keys)//2
        self.keys = all_keys[:median_index]
        sibling_node = B_node(self.parent, self.tree)
        sibling_node.keys = all_keys[median_index+1:]
        all_children = self.children
        children_index = len(all_children)//2
        self.children = all_children[:children_index]
        sibling_node.children = all_children[children_index:]
        for child in all_children[children_index:]:
            child.parent = sibling_node
        if not self.is_root():
            self.parent.children.insert(self.parent.children.index(self) + 1, sibling_node)
            self.parent.insert_key(all_keys[median_index])
        else:
            parent_node = B_node(self.parent, self.tree)
            parent_node.insert_key(all_keys[median_index])
            parent_node.children.append(self)
            parent_node.children.append(sibling_node)
            self.tree.root_node = parent_node
            self.parent = parent_node
            sibling_node.parent = parent_node
        # self.print_whole_tree()


    def is_leaf(self):
        '''
        checks if the current node is a leaf

        this function will return true if the current node is a leaf
        and return fals if not. It checks if the node has any children to
        know if it's a leaf.

        Parameters
        ----------
            None

        Returns
        -------
            None
        '''
        return True if self.children == [] else False


    def is_root(self):
        '''
        Checks if the current node is a root of tree

        It does this by checking the parent of its parent
        to see if it's equal to None. Since the parent of a tree
        is None

        Parameters
        ----------
            None

        Returns
        -------
            None
        '''
        return True if self.parent == None else False


    def __repr__(self):
        children_str = "" if self.is_leaf() else ", \"children\": " + str(self.children)
        return "{\"keys\": " + str(self.keys) + children_str + "}" 


    # http://ysangkok.github.io/js-clrs-btree/btree.html
    def __str__(self):
        '''
        The current representation have been modified in order to be visualized in:
        # http://ysangkok.github.io/js-clrs-btree/btree.html
        '''
        children_str = "" if self.is_leaf() else ", \"children\": " + str(self.children) 
        return "{\"keys\": " + str(self.keys) + children_str + "}"


    def print_whole_tree(self):
        '''
        This function will print the whole tree
        if enough time to implement animation function this
        function could come in handy
        '''
        root_node = self
        while root_node.parent != None:
            root_node = root_node.parent
        print(root_node)


    if __name__ == '__main__':
        main()

