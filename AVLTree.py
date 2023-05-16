# username - hilabarkan, guykoch
# id1      - 208239152
# name1    - hila barkan
# id2      - 318962909
# name2    - guy koch

from random import shuffle
import random

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""

	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0

	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""

	def get_key(self):
		return self.key

	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""

	def get_value(self):
		return self.value

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""

	def get_left(self):
		return self.left

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""

	def get_right(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

	def get_parent(self):
		return self.parent

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

	def get_height(self):
		return self.height

	"""returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""

	def get_size(self):
		return self.size

	"""sets key

	@type key: int or None
	@param key: key
	"""

	def set_key(self, key):
		self.key = key
		return self

	"""sets value

	@type value: any
	@param value: data
	"""

	def set_value(self, value):
		self.value = value
		return self

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""

	def set_left(self, node):
		self.left = node
		return self

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""

	def set_right(self, node):
		self.right = node
		return self

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""

	def set_parent(self, node):
		self.parent = node
		return self

	"""sets the height of the node

	@type h: int
	@param h: the height
	"""

	def set_height(self, h):
		self.height = h
		return self

	"""sets the size of node

	@type s: int
	@param s: the size
	"""

	def set_size(self, s):
		self.size = s
		return self

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

	def is_real_node(self):
		return self.key != None

	"""
	Convert node from virtual to real 
	"""

	def convert_node_to_real(self):
		node_left = AVLNode(None, None)
		node_right = AVLNode(None, None)
		node_left.set_parent(self)
		node_right.set_parent(self)
		self.set_height(0)
		self.set_size(1)
		self.set_left(node_left)  # virtual node
		self.set_right(node_right)  # virtual node


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
	"""
	Constructor, you are allowed to add more fields.

	"""

	def __init__(self):
		self.root = None

		# add your fields here
		self.max = None

	"""searches for a value in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: any
	@returns: the value corresponding to key.
	"""

	def search(self, key):
		node = self.get_root()
		while node is not None and node.is_real_node():
			if node.get_key() == key:
				return node
			elif node.get_key() > key:
				node = node.get_left()
			else:
				node = node.get_right()
		return None

	##################################################################################
	############################# Helper Methods #####################################

	# Creaets a node with the given key and val and inserts as usual BST
	def insert_node_bst(self, key, val):
		sub_tree_root_parent = self.root
		sub_tree_root = self.root
		node_to_insert = AVLNode(key, val)
		node_to_insert.convert_node_to_real()

		# the tree was empty
		if sub_tree_root == None:
			self.root = node_to_insert
			return node_to_insert

		while sub_tree_root.get_key() != None:
			sub_tree_root_parent = sub_tree_root
			if node_to_insert.get_key() < sub_tree_root.get_key():
				sub_tree_root = sub_tree_root.get_left()
			else:
				sub_tree_root = sub_tree_root.get_right()
		node_to_insert.set_parent(sub_tree_root_parent)

		if node_to_insert.get_key() < sub_tree_root_parent.get_key():
			sub_tree_root_parent.set_left(node_to_insert)
		else:
			sub_tree_root_parent.set_right(node_to_insert)

		return node_to_insert

	# Deletes leaf from tree, should be called with node that is a leaf.
	def delete_leaf(self, node):
		x = node.get_parent()
		if x.get_left() == node:
			x.set_left(AVLNode(None, None))
		else:
			x.set_right(AVLNode(None, None))
		return

	# Deletes node from tree if it has only one child.
	# Change pointers to bypass it.
	def delete_one_child(self, node):
		# If node has only right child
		if node.get_left().get_key() is None:
			node.get_right().set_parent(node.get_parent())
			if node.get_parent().get_key() > node.get_key():  # came from left
				node.get_parent().set_left(node.get_right())
			else:
				node.get_parent().set_right(node.get_right())
		# If node has only left child
		if node.get_right().get_key() is None:
			node.get_left().set_parent(node.get_parent())
			if node.get_parent().get_key() > node.get_key():  # came from left
				node.get_parent().set_left(node.get_left())
			else:
				node.get_parent().set_right(node.get_right())

		return

	def get_successor(self, node):
		if node.get_right().get_key() is not None:
			y = node.get_right()
			while y.get_left().get_key() is not None:
				y = y.get_left()
			return y
		y = node.get_parent()
		while y is not None and node == y.get_right():
			node = y
			y = node.get_parent()
		return y

	# Regular bst delete
	def delete_node_bst(self, node):
		# If node is leaf
		if node.get_left().get_key() is None and node.get_right().get_key() is None:
			self.delete_leaf(node)
		# If node has one child
		elif node.get_left().get_key() is None or node.get_right().get_key() is None:
			self.delete_one_child(node)
		# Hard case - node has two children
		else:
			y = self.get_successor(node)
			self.delete_one_child(y)
			node.set_key(y.get_key())
			node.set_value(y.get_value())
		return

	# returns the BF of a given node in the AVLTree
	def calculate_BF(self, node):
		if node.get_left().get_key() is None and node.get_right().get_key() is None:
			return 0
		elif node.get_left().get_key() is None:
			return (1 + node.get_right().get_height()) * (-1)
		elif node.get_right().get_key() is None:
			return node.get_left().get_height() + 1
		else:
			return node.get_left().get_height() - node.get_right().get_height()

	# Updates node size and height
	def update(self, node):
		node.set_size(1 + node.get_left().get_size() + node.get_right().get_size())
		node.set_height(1 + max(node.left.get_height(), node.right.get_height()))

	# Receives an AVL criminal node and calls the required rotation as we learned in class.
	def rotate(self, criminal_node, criminal_node_bf):

		criminal_son_bf = self.calculate_BF(criminal_node.get_left()) if criminal_node_bf == 2 else self.calculate_BF(
			criminal_node.get_right())

		if criminal_node_bf == 2:
			if criminal_son_bf == 1 or criminal_son_bf == 0:  # right rotation
				self.right_rotation(criminal_node)
				return 1
			else:  # left then right rotation
				self.left_rotation(criminal_node.get_left())
				self.right_rotation(criminal_node)
				return 2
		else:
			if criminal_son_bf == -1 or criminal_son_bf == 0:  # left rotation
				self.left_rotation(criminal_node)
				return 1
			else:  # right then left rotation
				self.right_rotation(criminal_node.get_right())
				self.left_rotation(criminal_node)
				return 2

	# Preform right rotation by changing pointers and update the relevant nodes.
	def right_rotation(self, node):
		y = node.get_left()
		if node.get_parent() is not None:
			if node.get_parent().get_key() > node.get_key():
				node.get_parent().set_left(y)
			else:
				node.get_parent().set_right(y)
			y.set_parent(node.get_parent())
		else:
			self.root = y
			y.set_parent(None)
		t = y.get_right()
		y.set_right(node)
		node.set_parent(y)
		node.set_left(t)
		t.set_parent(node)

		self.update(node)
		self.update(y)

	# Preform left rotation, same as right.
	def left_rotation(self, node):
		y = node.get_right()
		if node.get_parent() is not None:
			if node.get_parent().get_key() > node.get_key():
				node.get_parent().set_left(y)
			else:
				node.get_parent().set_right(y)
			y.set_parent(node.get_parent())
		else:
			self.root = y
			y.set_parent(None)
		t = y.get_left()
		y.set_left(node)
		node.set_parent(y)
		node.set_right(t)
		t.set_parent(node)

		self.update(node)
		self.update(y)

	# Fill a list with the given node subtree inorder scan.
	def inorder_rec(self, node, avl_list):
		if node != None and node.get_key() != None:
			self.inorder_rec(node.get_left(), avl_list)
			avl_list.append((node.get_key(), node.get_value()))
			self.inorder_rec(node.get_right(), avl_list)

	# Select using recursion, as we learned in class
	def select_rec(self, node, i):
		r = node.get_left().get_size() + 1
		if i == r:
			return node
		elif i < r:
			return self.select_rec(node.get_left(), i)
		else:
			return self.select_rec(node.get_right(), i - r)

	# Joins tree to self from left side, this means that self is bigger than tree and that self.keys>key>tree.keys
	def join_to_left(self, tree, key, val):
		height_diff = 0
		connector = AVLNode(key, val)
		connector.convert_node_to_real()
		node = self.get_root()
		while (node.get_height() > tree.get_root().get_height()):
			node = node.get_left()
			height_diff += 1
		parent = node.get_parent()
		connector.set_right(node)
		connector.set_left(tree.get_root())
		node.set_parent(connector)
		tree.get_root().set_parent(connector)
		connector.set_parent(parent)
		if parent is not None:
			parent.set_left(connector)
		# temp = connector
		# temp_son = None
		# while temp is not None:
		# 	self.update(temp)
		# 	temp_son = temp
		# 	temp = temp.get_parent()
		# self.root = temp_son

		# Rotating to balanced AVL tree
		node = connector
		temp = None
		while node is not None:
			bf = self.calculate_BF(node)
			if abs(bf) >= 2:
				self.rotate(node, bf)
			else:
				self.update(node)
			temp = node
			node = node.get_parent()
		self.root = temp
		return height_diff + 1

	def join_to_right(self, tree, key, val):
		height_diff = 0
		connector = AVLNode(key, val)
		connector.convert_node_to_real()
		node = self.get_root()
		while node.get_height() > tree.get_root().get_height():
			node = node.get_right()
			height_diff += 1
		parent = node.get_parent()
		connector.set_right(tree.get_root())
		connector.set_left(node)
		tree.get_root().set_parent(connector)
		node.set_parent(connector)
		connector.set_parent(parent)
		if parent is not None:
			parent.set_right(connector)

		# Rotating to balanced AVL tree
		node = connector
		temp = None
		while node is not None:
			bf = self.calculate_BF(node)
			if abs(bf) >= 2:
				self.rotate(node, bf)
			else:
				self.update(node)
			temp = node
			node = node.get_parent()
		self.root = temp

		return height_diff + 1

	##################################################################################
	##################################################################################

	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def insert(self, key, val):
		created_node = self.insert_node_bst(key, val)
		parent = created_node.get_parent()
		total_ops = 0
		while parent is not None:
			bf = self.calculate_BF(parent)
			if abs(bf) < 2:
				self.update(parent)
			else:
				total_ops = self.rotate(parent, bf)
			parent = parent.get_parent()
		return total_ops

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def delete(self, node):
		parent = node.get_parent()
		self.delete_node_bst(node)
		total_ops = 0
		while parent is not None:
			bf = self.calculate_BF(parent)
			if abs(bf) < 2:
				self.update(parent)
			else:
				total_ops += self.rotate(parent, bf)
			parent = parent.get_parent()
		return total_ops

	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""

	def avl_to_array(self):
		avl_list = []
		self.inorder_rec(self.root, avl_list)
		return avl_list

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""

	def size(self):
		if self.get_root() is None:
			return 0
		return self.get_root().get_size()

	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""

	def split(self, node):
		# Create smaller and bigger trees for the node
		smaller_tree = AVLTree()
		if node.get_left().is_real_node():
			smaller_tree.root = node.get_left()
			smaller_tree.root.set_parent(None)
		bigger_tree = AVLTree()
		if node.get_right().is_real_node():
			bigger_tree.root = node.get_right()
			bigger_tree.root.set_parent(None)

		# going up from node to root
		while node.get_parent() is not None:
			# node is right child to his parent, need to add the parents left child to "smaller tree"
			if node.get_key() > node.get_parent().get_key():
				node = node.get_parent()
				left_tree = AVLTree()
				if node.get_left().is_real_node():
					left_tree.root = node.get_left()
					left_tree.root.set_parent(None)
				else:
					left_tree.root = None
				height_diff = smaller_tree.join(left_tree, node.get_key(), node.get_value())
			else:
				# node is left child to his parent, need to add parents right child to "bigger tree"
				node = node.get_parent()
				right_tree = AVLTree()
				if node.get_right().is_real_node():
					right_tree.root = node.get_right()
					right_tree.root.set_parent(None)
				else:
					right_tree.root = None
				height_diff = bigger_tree.join(right_tree, node.get_key(), node.get_value())
		return [smaller_tree, bigger_tree]

	"""joins self with key and another AVLTree

	@type tree: AVLTree 
	@param tree: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree are larger than key,
	or the other way around.
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

	def join(self, tree, key, val):
		if self.get_root() is None and tree.get_root() is None:
			return 1
		if tree.get_root() is None:
			height = self.get_root().get_height()
			self.insert(key, val)
			return height + 1
		if self.get_root() is None:
			height = tree.get_root().get_height()
			tree.insert(key, val)
			self.root = tree.root
			return height + 1
		# self is higher
		if self.get_root().get_height() > tree.get_root().get_height():
			# self has bigger keys
			if self.get_root().get_key() > tree.get_root().get_key():  # self is bigger and taller
				height_diff = self.join_to_left(tree, key, val)
			else:  # self has smaller keys
				height_diff = self.join_to_right(tree, key, val)
		else:
			# self is shorter and has bigger keys
			if self.get_root().get_key() > tree.get_root().get_key():  # self is bigger and shorter
				height_diff = tree.join_to_right(self, key, val)
			else:  # self is shorter and has smaller keys
				height_diff = tree.join_to_left(self, key, val)
			self.root = tree.get_root()

		return height_diff

	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""

	def rank(self, node):
		r = node.get_left().get_size() + 1
		y = node
		while y:
			if y.get_parent() and y == y.get_parent().get_right():
				r += y.get_parent().get_left().get_size() + 1
			y = y.get_parent()
		return r

	"""finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""

	def select(self, i):
		x = self.get_root()
		return self.select_rec(x, i)

	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""

	def get_root(self):
		return self.root
