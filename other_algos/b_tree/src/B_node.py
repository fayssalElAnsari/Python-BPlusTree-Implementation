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
                for i in range(len(self.keys)):
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
            self.search_node(element).insert(element)  


    def insert_key(self, element):
        all_keys = self.keys.copy()
        all_keys.append(element)
        all_keys.sort(reverse=False)
        if len(all_keys) < self.m - 1:
            self.keys = all_keys
        else:
            self.split(element)


    def split(self, element):
        all_keys = self.keys.copy()
        all_keys.append(element)
        all_keys.sort(reverse=False)
        median_index = len(all_keys)//2
        self.keys = all_keys[:median_index]
        sibling_node = B_node(self.parent)
        sibling_node.keys = all_keys[median_index+1:]
        if not self.is_root():
            self.parent.insert_key(all_keys[median_index])
            self.parent.children.insert(self.parent.children.index(self) + 1, sibling_node)
        else:
            parent_node = B_node(self.parent)
            parent_node.insert_key(all_keys[median_index])
            parent_node.children.append(self)
            parent_node.children.append(sibling_node)
            self.parent.root_node = parent_node
            self.parent = parent_node
            sibling_node.parent = parent_node


    def is_leaf(self):
        return True if self.children == [] else False


    def is_root(self):
        return self.parent.parent == None


    def __repr__(self):
       return "Node :{keys=" + str(self.keys) + "; children=" + str(self.children) + "}" 


    def __str__(self):
        return "Node :{keys=" + str(self.keys) + "; children=" + str(self.children) + "}"


    if __name__ == '__main__':
        main()

