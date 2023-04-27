# username - hilabarkan, guykoch
# id1      - 208239152
# name1    - hila barkan
# id2      - 318962909
# name2    - guy koch

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
A class implementing an AVL tree.
"""


class AVLTree(object):
	"""
	Constructor, you are allowed to add more fields.

	"""

	def __init__(self):
		self.root = None

	# add your fields here

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
	############################# Helper Method For Insert ###########################

	# Creaets a node with the given key and val and inserts as usual BST
	def insert_node_bst(self, key, val):
		y = None
		x = self.root
		z_left = AVLNode(None, None)
		z_right = AVLNode(None, None)
		z = AVLNode(key, val)
		z.set_height(0)
		z.set_size(1)
		z.set_left(z_left)  # virtual node
		z.set_right(z_right)  # virtual node

		while x != None and x.get_key() != None:
			y = x
			# Fixing the size of the nodes on the way down
			y.set_size(y.get_size() + 1)
			if z.get_key() < x.get_key():
				x = x.get_left()
			else:
				x = x.get_right()
		z.set_parent(y)
		# the tree was empty
		if y == None:
			self.root = z
			return z
		else:
			if z.get_key() < y.get_key():
				y.set_left(z)
			else:
				y.set_right(z)

		# fixing the height of the relevant nodes going up again
		# need to fix height only when the parent has one child after insertion
		# id the new node has a brother then it doesn't change heights.
		if not (z.get_parent().get_left().is_real_node() and z.get_parent().get_right().is_real_node()):
			node = z.get_parent()
			tmpHeight = node.get_height()
			while node != None:
				if node.get_height() >= tmpHeight + 1:
					return z
				node.set_height(node.get_height() + 1)
				tmpHeight = node.get_height()
				node = node.get_parent()

		return z

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
		if node.get_right().get_key() is None:
			return None
		y = node.get_right()
		while y.get_left().get_key() is not None:
			y = y.get_left()
		return y

	# called after deletion
	def is_height_changed_after_delete(self, node, child):
		# deletion came from right
		if node.get_key() < child.get_key():
			return node.get_left().get_height() < 1 + node.get_right().get_height()
		# came from left
		else:
			return node.get_right().get_height() < 1 + node.get_left().get_height()

	# Regular bst delete. Doesn't consider AVL stuff
	# Updates size and height.
	def delete_node_bst(self, node):
		parent1 = node.get_parent()
		parent2 = node.get_parent()
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

		while parent1 is not None:
			# decrease size
			parent1.set_size(parent1.get_size() - 1)
			parent1 = parent1.get_parent()

		# if the deleted node was only child, need to check height diffrences
		if parent2.get_left().get_key() is None and parent2.get_right().get_key() is None:
			while parent2 is not None:
				if parent2.get_height() == max(parent2.get_left().get_height(), parent2.get_left().get_height()) + 1:
					return
				parent2.set_height(parent2.get_height() - 1)
				parent2 = parent2.get_parent()

		return

	# returns the BF of a given node in the AVLTree
	def calculate_BF(self, node):
		if node.get_left().get_key() == None and node.get_right().get_key() == None:
			return 0
		elif node.get_left().get_key() == None:
			return ((1 + node.get_right().get_height()) * (-1))
		elif node.right.key == None:
			return node.get_left().get_height() + 1
		else:
			return node.get_left().get_height() - node.get_right().get_height()

	# called after insertion and before a rotation, deretmines if the height of a given node has changed
	def is_height_changed(self, node, son_val):
		if node.get_key() < son_val:  # came from right
			return node.get_right().get_height() >= 1 + node.get_left().get_height()
		else:  # came from left
			return node.get_left().get_height() >= 1 + node.get_right().get_height()

	def rotate(self, criminal_node, criminal_node_bf, criminal_son_bf):
		if criminal_node_bf == 2:
			if criminal_son_bf == 1 or criminal_son_bf == 0:  # right rotation
				self.right_rotation(criminal_node)
				return 1
			else:  # left then right rotation
				self.left_rotation(criminal_node.left)
				self.right_rotation(criminal_node)
				return 2
		else:
			if criminal_son_bf == -1 or criminal_son_bf == 0:  # left rotation
				self.left_rotation(criminal_node)
				return 1
			else:  # right then left rotation
				self.right_rotation(criminal_node.right)
				self.left_rotation(criminal_node)
				return 2

	def right_rotation(self, node):
		y = node.get_left()
		if node.get_parent() != None:
			if node.get_parent().get_key() > node.get_key():  # node is left son to parent
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

		node.set_size(1 + node.get_left().get_size() + node.get_right().get_size())
		y.set_size(1 + y.get_left().get_size() + y.get_right().get_size())

		node.set_height(1 + max(node.left.get_height(), node.right.get_height()))
		# y.set_height(1 + max(y.left.get_height(), y.right.get_height()))

		while y != None:
			y.set_height(1 + max(y.left.get_height(), y.right.get_height()))
			y = y.get_parent()

	def left_rotation(self, node):
		y = node.get_right()  # 7
		if node.get_parent() != None:
			if node.get_parent().get_key() > node.get_key():  # node is left son to parent
				node.get_parent().set_left(y)
			else:
				node.get_parent.set_right(y)
			y.set_parent(node.get_parent())
		else:
			self.root = y
			y.set_parent(None)
		t = y.get_left()
		y.set_left(node)
		node.set_parent(y)
		node.set_right(t)
		t.set_parent(node)

		node.set_size(1 + node.get_left().get_size() + node.get_right().get_size())
		y.set_size(1 + y.get_left().get_size() + y.get_right().get_size())

		node.set_height(1 + max(node.left.get_height(), node.right.get_height()))

		while y != None:
			y.set_height(1 + max(y.left.get_height(), y.right.get_height()))
			y = y.get_parent()
			
	def inorder_rec(self, node, avl_list):
		if node != None and node.get_key() != None:
			self.inorder_rec(node.get_left(), avl_list)
			avl_list.append((node.get_key(), node.get_value()))
			self.inorder_rec(node.get_right(), avl_list)
			

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
		x = created_node
		y = created_node.get_parent()
		total_ops = 0
		while y != None:
			bf = self.calculate_BF(y)
			if abs(bf) < 2 and not self.is_height_changed(y, x.key):
				return 0
			elif abs(bf) < 2 and self.is_height_changed(y, x.key):
				y = y.get_parent()
				x = x.get_parent()
			else:
				criminal_son_bf = self.calculate_BF(y.get_left()) if bf == 2 else self.calculate_BF(y.get_right())
				total_ops = self.rotate(y, bf, criminal_son_bf)
				break
		return total_ops

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def delete(self, node):
		y = node.get_parent()
		self.delete_node_bst(node)
		total_ops = 0
		while y is not None:
			bf = self.calculate_BF(y)
			if abs(bf) < 2 and not self.is_height_changed_after_delete(y, node):
				return 0
			elif abs(bf) < 2 and self.is_height_changed_after_delete(y, node):
				y = y.get_parent()
			else:
				criminal_son_bf = self.calculate_BF(y.get_left() if bf == 2 else self.calculate_BF(y.get_right))
				total_ops += self.rotate(y, bf, criminal_son_bf)
				y = y.get_parent()
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
		return None

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
		return None

	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""

	def rank(self, node):
		return None

	"""finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""

	def select(self, i):
		return None

	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""

	def get_root(self):
		return self.root
