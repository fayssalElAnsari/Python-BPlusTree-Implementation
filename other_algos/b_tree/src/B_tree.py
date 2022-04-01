from B_node import B_node

class B_tree:
    def __init__(self, m):
        '''
        Constructor for the B_tree class

        This function creates a tree of higher degree m and lower degree l=[m/2]
        the B tree contains a root node which is an instance of the class B_node
        The root node takes in this class (B_tree) as a parent. And a parent of None
        Therefore the way to check whether or not a node is a root node is its parent 
        of parent == None

        Parameters
        ----------
        m : int
            The degree of the B_tree
            which is also the maximum number of children
            and the maximum number of keys + 1

        Returns
        -------
            B_tree instance
        '''
        self.m = m
        self.l = m//2
        self.root_node = B_node(None, self)
        

    def search_element(self, element):
        '''
        Search for an element in the tree

        This function will check if an element exists in a given tree.
        The way it works is by simply calling the search_element function
        on its root node

        Parameters
        ----------
        element : int
            The element to be checked if it exists in the current B_tree

        Returns
        -------
            true: if the element exists
            false: if the element doesn't exist in the tree
        '''
        self.root_node.search_element(element)
        

    def search_node(self, element):
        '''
        Search for a node containing the given element

        This function will check in which node the element exists in this tree.
        The way it works is by simply calling the search_node function
        on its root node

        Parameters
        ----------
        element : int
            The element to look for in this tree

        Returns
        -------
            A B_node object containing either the node that contains the 
            given element or the node in which that element should be if
            it did exist
        '''
        self.root_node.search_node(element)

    
    def insert(self, element):
        '''
        Search for an element in the tree

        This function will check if an element exists in a given tree.
        The way it works is by simply calling the search_element function
        on its root node

        Parameters
        ----------
        element : int
            The element to be checked if it exists in the current B_tree

        Returns
        -------
            true: if the element exists
            false: if the element doesn't exist in the tree
        '''
        self.root_node.insert(element)


    def delete(self, element):
        '''
        Search for an element in the tree then deletes it

        This function will check if an element exists and delete it
        The way it works is by simply calling the delete function
        on its root node

        Parameters
        ----------
        element : int
            The element to be deleted if it exists in the current B_tree

        Returns
        -------
            None
        '''
        self.root_node.delete(element)


    def main():
        print("B_tree")

    
    def digraph(self):
        header1 = "digraph {"
        header2 = "node [shape = record, height=.1];"
        arcs = ""
        nodes = ""
        body = ""
        footer = " }"    
        return header1 + header2 + body + footer


    def depth_first_search(self, key_list=[]):
        for child in node.children:
            key_list.append(child.keys)
            result =  child.depth_first_search(key_list)
            return result


    def breadth_first_search(self):
        pass


    def __repr__(self):
       return "{\"keys\": " + str(self.root_node.keys) + ", \"children\": "+str(self.root_node.children) +"}" 


    def __str__(self):
        return "{\"keys\": " + str(self.root_node.keys) + ", \"children\": "+str(self.root_node.children) +"}"
        

    if __name__ == '__main__':
        main()