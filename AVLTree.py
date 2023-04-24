#username - hilabarkan, guykoch
#id1      - 208239152 
#name1    - hila barkan 
#id2      - 318962909
#name2    - guy koch  

import math

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
		node = self.root
		while(node != None):
			if node.key == key:
				return node
			elif node.key > key:
				node = node.left
			else:
				node = node.right
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
		z.set_left(z_left) # virtual node
		z.set_right(z_right) # virtual node

		while x != None and x.key != None:
			y = x
			# Fixing the size of the nodes on the way down
			y.size += 1
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.parent = y
		# the tree was empty
		if y == None:
			self.root = z
			return z
		else:
			if z.key < y.key:
				y.left = z
			else:
				y.right = z
		
		# fixing the height of the relevant nodes going up again
		# need to fix height only when the parant way a leaf and not it is a not
		if not(z.parent.left.is_real_node() and  z.parent.right.is_real_node()): 
			node = z.parent
			tmpHeight = node.height
			while node != None:
				if node.height >= tmpHeight + 1:
					return z
				node.height += 1
				tmpHeight = node.height
				node = node.parent
				
		return z
		
	# returns the BF of a given node in the AVLTree		
	def calculate_BF(self, node):
		if node.left.key == None and node.right.key == None:
			return 0
		elif node.left.key == None:
			return ((1 + node.right.get_height()) * (-1))
		elif node.right.key == None:
			return node.left.get_height() + 1 
		else:
			return node.left.height - node.right.height
	

	# called after insertion and before a rotation, deretmines if the height of a given node has changed
	def is_height_changed(self, node, son_val):
		if node.key < son_val: # came from right
			return node.right.height >= 1 + node.left.height
		else: # came from left
			return node.left.height >= 1 + node.right.height

	def rotate(self, criminal_node, criminal_node_bf, criminal_son_bf):
		if criminal_node_bf == 2:
			if criminal_son_bf == 1: # right rotation
				self.right_rotation(criminal_node)
			else: # left then right rotation
				self.left_rotation(criminal_node.left)
				self.right_rotation(criminal_node)
		else:
			if criminal_son_bf == -1 : # left rotation
				self.left_rotation(criminal_node)
			else: # right then left rotation
				self.right_rotation(criminal_node.right)
				self.left_rotation(criminal_node)

	def right_rotation(self, node):
		y = node.left # 7
		if node.parent != None:
			if node.parent.key > node.key: # node is left son to parent
				node.parent.left = y
			else:
				node.parent.right = y
			y.parent = node.parent
		else:
			self.root = y
			y.parent = None
		t = y.right # t is 7 right son
		y.right = node # 7.right = 8
		node.parent = y # 8.parent = 7
		node.left = t # 8.left = 7.right
		t.parent = node # 7.right.parent = t = 8

		node.set_size(1 + node.left.size + node.right.size)
		y.set_size(1 + y.left.size + y.right.size)

		node.set_height(1 + max(node.left.get_height(), node.right.get_height()))
		#y.set_height(1 + max(y.left.get_height(), y.right.get_height()))

		while y != None:
			y.set_height(1 + max(y.left.get_height(), y.right.get_height()))
			y = y.parent


	def left_rotation(self, node):
		y = node.right # 7
		if node.parent != None:
			if node.parent.key > node.key: # node is left son to parent
				node.parent.left = y
			else:
				node.parent.right = y
			y.parent = node.parent
		else:
			self.root = y
			y.parent = None
		t = y.left # t is 7 left son
		y.left = node # 7.left = 8
		node.parent = y # 6.parent = 7
		node.right = t # 6.right = 7.left
		t.parent = node # 7.right.parent = t = 8

		node.set_size(1 + node.left.size + node.right.size)
		y.set_size(1 + y.left.size + y.right.size)

		node.set_height(1 + max(node.left.get_height(), node.right.get_height()))
		#y.set_height(1 + max(y.left.get_height(), y.right.get_height()))

		while y != None:
			y.set_height(1 + max(y.left.get_height(), y.right.get_height()))
			y = y.parent


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
		y = created_node.parent
		while y != None:
			bf = self.calculate_BF(y)
			if abs(bf) < 2 and not self.is_height_changed(y, x.key):
				break
			elif abs(bf) < 2 and self.is_height_changed(y, x.key):
				y = y.parent
				x = x.parent
			else:
				criminal_son_bf = self.calculate_BF(y.left) if bf == 2 else self.calculate_BF(y.right)
				self.rotate(y, bf, criminal_son_bf)
				break
		return -1

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		return -1


	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


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
		return None
