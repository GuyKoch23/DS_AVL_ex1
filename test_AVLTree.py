from AVLTree import AVLTree
import pytest

def print_visual_tree(node):
    pass

def print_inorder(node):
    if node != None and node.key != None:
        print_inorder(node.left)
        print(node.key, "height = " + str(node.height), "size = " + str(node.size))
        print_inorder(node.right)

def build_tree(tree_keys_list):
    tree = AVLTree()
    for key in tree_keys_list:
        tree.insert_node_bst(key,key)
    return tree

def build_trees(trees_keys_list):
    trees_list = []
    for tree_keys_list in trees_keys_list:
        builded_tree = build_tree(tree_keys_list)
        trees_list.append(builded_tree)
    return trees_list


def visual_trees():
    
    ### config ###############################################################
    tree1_keys = ([15,10,22,4,11,20,24,2,7,12,18,1,6,8], True)
    tree2_keys = ([6,8], False)
    tree3_keys = ([], False)
    tree4_keys = ([5,6,7,8], False)

    trees_tuples_list = [tree1_keys, tree2_keys, tree3_keys, tree4_keys]

    trees_keys_list = [tree[0] for tree in trees_tuples_list if tree[1] == True]


    ### Create Trees ##########################################################
    trees_list = build_trees(trees_keys_list)
    
        # for i in range(len(trees)) :
    #     print('tree '+str(i+1))
    #     print_inorder(trees[i].root)
    #     print(" ")
    #     trees[i].insert(7,7)
    #     print_inorder(trees[i].root)
    #     #trees[i].right_rotation(trees[i].root)



####################################### Testers ##############################

### Test Build method ###
def test_build_876():
    tree = build_tree([8,7,6])
    # Keys of the tree
    assert(tree.get_root().get_key() == 8)
    assert(tree.get_root().get_left().get_key() == 7)
    assert(tree.get_root().get_left().get_left().get_key() == 6)
    # Sizes of the tree
    assert(tree.get_root().get_size() == 3)
    assert(tree.get_root().get_left().get_size() == 2)
    assert(tree.get_root().get_left().get_left().get_size() == 1)
    # Heights of the tree
    assert(tree.get_root().get_height() == 2)
    assert(tree.get_root().get_left().get_height() == 1)
    assert(tree.get_root().get_left().get_left().get_height() == 0)

def test_build_678():
    tree = build_tree([6,7,8])
    # Keys of the tree
    assert(tree.get_root().get_key() == 6)
    assert(tree.get_root().get_right().get_key() == 7)
    assert(tree.get_root().get_right().get_right().get_key() == 8)
    # Sizes of the tree
    assert(tree.get_root().get_size() == 3)
    assert(tree.get_root().get_right().get_size() == 2)
    assert(tree.get_root().get_right().get_right().get_size() == 1)
    # Heights of the tree
    assert(tree.get_root().get_height() == 2)
    assert(tree.get_root().get_right().get_height() == 1)
    assert(tree.get_root().get_right().get_right().get_height() == 0)

def test_build_786():
    tree = build_tree([7,8,6])
    # Keys of the tree
    assert(tree.get_root().get_key() == 7)
    assert(tree.get_root().get_left().get_key() == 6)
    assert(tree.get_root().get_right().get_key() == 8)
    # Sizes of the tree
    assert(tree.get_root().get_size() == 3)
    assert(tree.get_root().get_left().get_size() == 1)
    assert(tree.get_root().get_right().get_size() == 1)
    # Heights of the tree
    assert(tree.get_root().get_height() == 1)
    assert(tree.get_root().get_left().get_height() == 0)
    assert(tree.get_root().get_right().get_height() == 0)

def test_build_768():
    tree = build_tree([7,6,8])
    # Keys of the tree
    assert(tree.get_root().get_key() == 7)
    assert(tree.get_root().get_left().get_key() == 6)
    assert(tree.get_root().get_right().get_key() == 8)
    # Sizes of the tree
    assert(tree.get_root().get_size() == 3)
    assert(tree.get_root().get_left().get_size() == 1)
    assert(tree.get_root().get_right().get_size() == 1)
    # Heights of the tree
    assert(tree.get_root().get_height() == 1)
    assert(tree.get_root().get_left().get_height() == 0)
    assert(tree.get_root().get_right().get_height() == 0)

### Test Search method ###

def test_search_8_in_678():
    tree = build_tree([6,7,8])
    node = tree.search(8)
    assert(node != None)
    assert(node.get_key() == 8)

def test_search_7_in_678():
    tree = build_tree([6,7,8])
    node = tree.search(7)
    assert(node != None)
    assert(node.get_key() == 7)

def test_search_7_in_768():
    tree = build_tree([7,6,8])
    node = tree.search(7)
    assert(node != None)
    assert(node.get_key() == 7)

def test_search_5_in_768():
    tree = build_tree([7,6,8])
    node = tree.search(5)
    assert(node == None)


### Test Insert method ###

def test_insert_6_to_87():
    tree = build_tree([8,7])
    tree.insert(6,6)
    # Keys of the tree
    assert(tree.get_root().get_key() == 7)
    assert(tree.get_root().get_left().get_key() == 6)
    assert(tree.get_root().get_right().get_key() == 8)
    # Sizes of the tree
    assert(tree.get_root().get_size() == 3)
    assert(tree.get_root().get_left().get_size() == 1)
    assert(tree.get_root().get_right().get_size() == 1)
    # Heights of the tree
    assert(tree.get_root().get_height() == 1)
    assert(tree.get_root().get_left().get_height() == 0)
    assert(tree.get_root().get_right().get_height() == 0)

def test_insert_8_to_67():
    tree = build_tree([6,7])
    tree.insert(8,8)
    # Keys of the tree
    assert(tree.get_root().get_key() == 7)
    assert(tree.get_root().get_left().get_key() == 6)
    assert(tree.get_root().get_right().get_key() == 8)
    # Sizes of the tree
    assert(tree.get_root().get_size() == 3)
    assert(tree.get_root().get_left().get_size() == 1)
    assert(tree.get_root().get_right().get_size() == 1)
    # Heights of the tree
    assert(tree.get_root().get_height() == 1)
    assert(tree.get_root().get_left().get_height() == 0)
    assert(tree.get_root().get_right().get_height() == 0)


#############################################################################

def main():
    pass
    
if __name__ == "__main__":
    main()