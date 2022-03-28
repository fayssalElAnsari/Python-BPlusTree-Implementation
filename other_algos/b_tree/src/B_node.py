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
            return true
        else:
            if self.is_leaf():
                return false
            else:
                for i in range(len(self.keys) - 1):
                    if element < keys[i]:
                        return self.children[i].search_element(element)
                        break
                return self.children[-1].search_element(element)
        

    def search_node(self, element):
        if self.is_leaf():
            return self
        else:
            for i in range(len(self.keys) - 1):
                if element < keys[i]:
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
        all_keys.sort(reverse=false)
        if len(all_keys) < self.m - 1:
            self.keys = all_keys
        else:
            self.split(element)

    def split(self, element):
        

    def is_leaf(self):
        return true if self.children == [] else false

    if __name__ == '__main__':
        main()