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
        tree.insert_node_bst(key, key)
    return tree


def build_trees(trees_keys_list):
    trees_list = []
    for tree_keys_list in trees_keys_list:
        builded_tree = build_tree(tree_keys_list)
        trees_list.append(builded_tree)
    return trees_list


def visual_trees():
    ### config ###############################################################
    tree1_keys = ([15, 10, 22, 4, 11, 20, 24, 2, 7, 12, 18, 1, 6, 8], True)
    tree2_keys = ([6, 8], False)
    tree3_keys = ([], False)
    tree4_keys = ([5, 6, 7, 8], False)

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
    tree = build_tree([8, 7, 6])
    # Keys of the tree
    assert (tree.get_root().get_key() == 8)
    assert (tree.get_root().get_left().get_key() == 7)
    assert (tree.get_root().get_left().get_left().get_key() == 6)
    # Sizes of the tree
    assert (tree.get_root().get_size() == 3)
    assert (tree.get_root().get_left().get_size() == 2)
    assert (tree.get_root().get_left().get_left().get_size() == 1)
    # Heights of the tree
    assert (tree.get_root().get_height() == 2)
    assert (tree.get_root().get_left().get_height() == 1)
    assert (tree.get_root().get_left().get_left().get_height() == 0)


def test_build_678():
    tree = build_tree([6, 7, 8])
    # Keys of the tree
    assert (tree.get_root().get_key() == 6)
    assert (tree.get_root().get_right().get_key() == 7)
    assert (tree.get_root().get_right().get_right().get_key() == 8)
    # Sizes of the tree
    assert (tree.get_root().get_size() == 3)
    assert (tree.get_root().get_right().get_size() == 2)
    assert (tree.get_root().get_right().get_right().get_size() == 1)
    # Heights of the tree
    assert (tree.get_root().get_height() == 2)
    assert (tree.get_root().get_right().get_height() == 1)
    assert (tree.get_root().get_right().get_right().get_height() == 0)


def test_build_786():
    tree = build_tree([7, 8, 6])
    # Keys of the tree
    assert (tree.get_root().get_key() == 7)
    assert (tree.get_root().get_left().get_key() == 6)
    assert (tree.get_root().get_right().get_key() == 8)
    # Sizes of the tree
    assert (tree.get_root().get_size() == 3)
    assert (tree.get_root().get_left().get_size() == 1)
    assert (tree.get_root().get_right().get_size() == 1)
    # Heights of the tree
    assert (tree.get_root().get_height() == 1)
    assert (tree.get_root().get_left().get_height() == 0)
    assert (tree.get_root().get_right().get_height() == 0)


def test_build_768():
    tree = build_tree([7, 6, 8])
    # Keys of the tree
    assert (tree.get_root().get_key() == 7)
    assert (tree.get_root().get_left().get_key() == 6)
    assert (tree.get_root().get_right().get_key() == 8)
    # Sizes of the tree
    assert (tree.get_root().get_size() == 3)
    assert (tree.get_root().get_left().get_size() == 1)
    assert (tree.get_root().get_right().get_size() == 1)
    # Heights of the tree
    assert (tree.get_root().get_height() == 1)
    assert (tree.get_root().get_left().get_height() == 0)
    assert (tree.get_root().get_right().get_height() == 0)


### Test Search method ###

def test_search_8_in_678():
    tree = build_tree([6, 7, 8])
    node = tree.search(8)
    assert (node != None)
    assert (node.get_key() == 8)


def test_search_7_in_678():
    tree = build_tree([6, 7, 8])
    node = tree.search(7)
    assert (node != None)
    assert (node.get_key() == 7)


def test_search_7_in_768():
    tree = build_tree([7, 6, 8])
    node = tree.search(7)
    assert (node != None)
    assert (node.get_key() == 7)


def test_search_5_in_768():
    tree = build_tree([7, 6, 8])
    node = tree.search(5)
    assert (node == None)


### Test Insert method ###

def test_insert_6_to_87():
    tree = build_tree([8, 7])
    tree.insert(6, 6)
    # Keys of the tree
    assert (tree.get_root().get_key() == 7)
    assert (tree.get_root().get_left().get_key() == 6)
    assert (tree.get_root().get_right().get_key() == 8)
    # Sizes of the tree
    assert (tree.get_root().get_size() == 3)
    assert (tree.get_root().get_left().get_size() == 1)
    assert (tree.get_root().get_right().get_size() == 1)
    # Heights of the tree
    assert (tree.get_root().get_height() == 1)
    assert (tree.get_root().get_left().get_height() == 0)
    assert (tree.get_root().get_right().get_height() == 0)


def test_insert_8_to_67():
    tree = build_tree([6, 7])
    tree.insert(8, 8)
    # Keys of the tree
    assert (tree.get_root().get_key() == 7)
    assert (tree.get_root().get_left().get_key() == 6)
    assert (tree.get_root().get_right().get_key() == 8)
    # Sizes of the tree
    assert (tree.get_root().get_size() == 3)
    assert (tree.get_root().get_left().get_size() == 1)
    assert (tree.get_root().get_right().get_size() == 1)
    # Heights of the tree
    assert (tree.get_root().get_height() == 1)
    assert (tree.get_root().get_left().get_height() == 0)
    assert (tree.get_root().get_right().get_height() == 0)


def test_delete_bst_8_from_678():
    tree = build_tree([6, 7, 8])
    tree.delete_node_bst(tree.get_root().get_right().get_right())
    # Keys of the tree
    assert (tree.get_root().get_key() == 6)
    assert (tree.get_root().get_right().get_key() == 7)
    assert (tree.get_root().get_right().get_right().get_key() is None)
    # Sizes of the tree
    assert (tree.get_root().get_size() == 2)
    assert (tree.get_root().get_right().get_size() == 1)
    assert (tree.get_root().get_right().get_right().get_size() == 0)
    # Heights of the tree
    assert (tree.get_root().get_height() == 1)
    assert (tree.get_root().get_right().get_height() == 0)
    assert (tree.get_root().get_right().get_right().get_height() == -1)


def test_delete_bst_6_from_5346():
    tree = build_tree([5, 3, 4, 6])
    tree.delete_node_bst(tree.get_root().get_right())
    # Keys of the tree
    assert (tree.get_root().get_right().get_key() is None)
    assert (tree.get_root().get_key() == 5)
    assert (tree.get_root().get_left().get_key() == 3)
    assert (tree.get_root().get_size() == 3)
    assert (tree.get_root().get_height() == 2)


def test_delete_bst_4_from_5346():
    tree = build_tree([5, 3, 4, 6])
    tree.delete_node_bst(tree.get_root().get_left().get_right())
    # Keys of the tree
    assert (tree.get_root().get_left().get_right().get_key() is None)
    assert (tree.get_root().get_left().get_height() == 0)
    assert (tree.get_root().get_height() == 1)


def test_delete_bst_7_from_54768():
    tree = build_tree([5, 4, 7, 6, 8])
    tree.delete_node_bst(tree.get_root().get_right())
    # Keys of the tree
    assert (tree.get_root().get_size() == 4)
    assert (tree.get_root().get_height() == 2)


def test_height_changed_deleting_8_in_5346():
    tree = build_tree([5, 3, 4, 6])
    to_delete_node = tree.get_root().get_left().get_right()
    tree.delete_node_bst(to_delete_node)
    # Keys of the tree
    assert (tree.is_height_changed_after_delete(tree.get_root(), to_delete_node))


def test_delete_24_in_bt():
    tree = build_tree([15, 8, 22, 4, 11, 20, 24, 2, 9, 12, 18, 13])
    to_delete_node = tree.get_root().get_right().get_right()
    number_of_rotations_performed = tree.delete(to_delete_node)
    # Keys of the tree
    assert (tree.get_root().get_height() == 3)
    assert (tree.get_root().get_key() == 11)
    assert (number_of_rotations_performed == 3)

def test_avl_to_list_bt():
    tree = build_tree([15, 8, 22, 4, 11, 20, 24, 2, 9, 12, 18, 13])
    avl_list = tree.avl_to_array()
    # Keys of the tree
    print(avl_list)
    assert (avl_list == [(2,2), (4,4), (8,8), (9,9), (11,11), (12,12), (13,13), (15,15), (18,18), (20,20), (22,22), (24,24)] )

#############################################################################

def main():
    pass


if __name__ == "__main__":
    main()
