import sys
import os
sys.path.append(os.path.abspath('../src'))
import B_tree
import unittest


class test_b_tree(unittest.TestCase):
    def setUp(self):
        

    def test_all_keys_increasing_order(self):

        pass

    def test_all_leafs_have_no_children(self):
        pass

    def test_all_internal_nodes_have_at_most_n_minus_one_keys(self):
        pass

    def test_all_internal_nodes_have_at_most_n_children(self):
        pass

    def test_all_internal_nodes_have_at_least_n_over_two_children(self):
        pass

    def all_leaves_have_same_depth(self):
        pass

    def root_node_have_minimum_of_one_key(self):
        pass

    def all_non_leaf_nodes_have_at_least_two_children(self):
        pass
    
    def non_leaf_node_with_k_minus_one_keys_contains_k_children(self):
        pass


if __name__ == '__main__':
    unittest.main()