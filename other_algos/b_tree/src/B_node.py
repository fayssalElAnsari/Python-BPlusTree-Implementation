class B_node:
    def main():
        print("B_node")


    def __init__(self, parent):
        self.parent = parent
        self.keys = []
        self.children = []
        self.m = parent.m
        self.l = parent.l
        

    def search_element(self, element):
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
        if self.is_leaf():
            return self
        else:
            for i in range(len(self.keys)):
                if element < self.keys[i]:
                    return self.children[i].search_node(element)
                    break
            return self.children[-1].search_node(element)


    def insert(self, element):
        if self.is_leaf():
            self.insert_key(element)
        else:
            (self.search_node(element)).insert(element)  


    def insert_key(self, element):
        all_keys = self.keys.copy()
        all_keys.append(element)
        all_keys.sort(reverse=False)
        if len(all_keys) < self.m:
            self.keys = all_keys
        else:
            self.split(element)


    def delete_key(self, element):
        self.keys.delete(element)


    def split(self, element):
        self.print_whole_tree()
        all_keys = self.keys.copy()
        all_keys.append(element)
        all_keys.sort(reverse=False)
        median_index = len(all_keys)//2
        self.keys = all_keys[:median_index]
        sibling_node = B_node(self.parent)
        sibling_node.keys = all_keys[median_index+1:]
        all_children = self.children
        children_index = len(all_children)//2
        self.children = all_children[:children_index]
        sibling_node.children = all_children[children_index:]
        if not self.is_root():
            self.parent.children.insert(self.parent.children.index(self) + 1, sibling_node)
            self.parent.insert_key(all_keys[median_index])
            self.print_whole_tree()
        else:
            parent_node = B_node(self.parent)
            parent_node.insert_key(all_keys[median_index])
            parent_node.children.append(self)
            parent_node.children.append(sibling_node)
            self.parent.root_node = parent_node
            self.parent = parent_node
            sibling_node.parent = parent_node
            self.print_whole_tree()


    def delete(self, element):
        self.search_node(element).delete_key(element)


    def is_leaf(self):
        return True if self.children == [] else False


    def is_root(self):
        return self.parent.parent == None


    def __repr__(self):
        children_str = "" if self.is_leaf() else ", \"children\": " + str(self.children)
        return "{\"keys\": " + str(self.keys) + children_str + "}" 


    # http://ysangkok.github.io/js-clrs-btree/btree.html
    def __str__(self):
        children_str = "" if self.is_leaf() else ", \"children\": " + str(self.children) 
        return "{\"keys\": " + str(self.keys) + children_str + "}"


    def print_whole_tree(self):
        '''
        if enough time to implement animation function this
        function could come in handy
        '''
        root_node = self
        while root_node.parent != None:
            root_node = root_node.parent
        print(root_node)

    if __name__ == '__main__':
        main()

