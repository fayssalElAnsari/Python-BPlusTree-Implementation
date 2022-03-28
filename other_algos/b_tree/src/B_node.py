class B_node:
    def main():
        print("B_node")

    def __init__(self, parent):
        self.parent = parent
        self.keys = []
        self.children = []
        

    def search_element(self, element):
        if element in self.keys:
            return true
        else:
            if self.is_leaf():
                return false
            else:
                for i in range(len(self.keys) - 1):
                    if element < keys[i]:
                        self.children[i].search_element(element)
                        break
                self.children[-1].search_element(element)
        

    def search_node(self, element):
        if self.is_leaf():
            return self
        else:
            for i in range(len(self.keys) - 1):
                if element < keys[i]:
                    self.children[i].search_node(element)
                    break
            self.children[-1].search_node(element) 


    def is_leaf(self):
        return true if self.children == [] else false

    if __name__ == '__main__':
        main()