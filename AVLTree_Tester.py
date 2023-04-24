#from AVLTree import * 
import AVLTree
from AVLTree import AVLTree as av


def runner():
    trees = construct_trees()
    for i in range(len(trees)) :
        print('tree '+str(i+1))
        print_inorder(trees[i].root)
        print(" ")
        trees[i].insert(7,7)
        print_inorder(trees[i].root)
        #trees[i].right_rotation(trees[i].root)

    

def print_inorder(node):
    if node != None and node.key != None:
        print_inorder(node.left)
        print(node.key, "height = " + str(node.height), "size = " + str(node.size))
        print_inorder(node.right)

def construct_trees():
    #tree_args1 = [15,10,22,4,11,20,24,2,7,12,18,1,6,8]
    tree1_args = [6,8]
    #tree3_args = []
    #tree4_args = [5,6,7,8]
    tree1 = create_tree(tree1_args)
    #tree2 = create_tree(tree2_args)
    #tree3 = create_tree(tree3_args)
    #tree4 = create_tree(tree4_args)
    #return [tree1, tree2, tree3, tree4]
    return [tree1]

def create_tree(keys_list):
    AVL_tree = av()
    for key in keys_list:
        a = AVL_tree.insert_node_bst(key,key)
    return AVL_tree

runner()