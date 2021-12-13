import time

from Queue import PriorityQueue

goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

INFINITY = 50000
maxnodes = 1

def board_state(state):
	i=0
#	temp=zeros([3,3])
	temp=[([0] * 3) for j in range(3)]
	for row in range(3):
         for col in range(3):
            temp[row][col] = state[i]
            i+=1
	return temp
	
    
def display_board( state ):
	print "-------------"
	print "| %i | %i | %i |" % (state[0], state[1], state[2])
	print "-------------"
	print "| %i | %i | %i |" % (state[3], state[4], state[5])
	print "-------------"
	print "| %i | %i | %i |" % (state[6], state[7], state[8])
	print "-------------"

	
def move_up( state ):
	"""Moves the blank tile up on the board. Returns a new state as a list."""
	# Perform an object copy
	new_state = state[:]
	index = new_state.index( 0 )
	# Sanity check
	if index not in [0, 1, 2]:
		# Swap the values.
		temp = new_state[index - 3]
		new_state[index - 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		# Can't move, return None (Pythons NULL)
		return None

def move_down( state ):
	"""Moves the blank tile down on the board. Returns a new state as a list."""
	# Perform object copy
	new_state = state[:]
	index = new_state.index( 0 )
	# Sanity check
	if index not in [6, 7, 8]:
		# Swap the values.
		temp = new_state[index + 3]
		new_state[index + 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		# Can't move, return None.
		return None

def move_left( state ):
	"""Moves the blank tile left on the board. Returns a new state as a list."""
	new_state = state[:]
	index = new_state.index( 0 )
	# Sanity check
	if index not in [0, 3, 6]:
		# Swap the values.
		temp = new_state[index - 1]
		new_state[index - 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		# Can't move it, return None
		return None

def move_right( state ):
	"""Moves the blank tile right on the board. Returns a new state as a list."""
	# Performs an object copy. Python passes by reference.
	new_state = state[:]
	index = new_state.index( 0 )
	# Sanity check
	if index not in [2, 5, 8]:
		# Swap the values.
		temp = new_state[index + 1]
		new_state[index + 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		# Can't move, return None
		return None

def create_node( state, parent, operator, depth, cost ):
	return Node( state, parent, operator, depth, cost )

def expand_node( node ):
	"""Returns a list of expanded nodes"""
	expanded_nodes = []
	expanded_nodes.append( create_node( move_up( node.state ), node, "up", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_down( node.state ), node, "down", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_left( node.state ), node, "left", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_right( node.state), node, "right", node.depth + 1, 0 ) )
	# Filter the list and remove the nodes that are impossible (move function returned None)
	expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
	return expanded_nodes
 
def dls( start, goal, depth=20):
	"""Performs the depth limit search. """  
	depth_limit = depth
	# A list (can act as a stack too) for the nodes.
	nodes = []
	# Create the queue with the root node in it.
	nodes.append( create_node( start, None, None, 0, 0 ) )
	count=0
	explored = []
	while nodes:
		# take the node from the front of the queue
		node = nodes.pop(0)
		count+=1
		explored.append(node.getState())
		print "Trying state", node.state, " and move: ", node.operator
		# if this node is the goal, return the moves it took to get here.
		if node.state == goal:
			print "done"
			print "The number of nodes visited",count
			print "States of moves are as follows:"
			return node.pathFromStart()
		if node.depth < depth_limit:
			expanded_nodes = expand_node(node)
			for item in expanded_nodes:
			    state = item.getState()
			    if state not in explored:
			        nodes.insert(0, item)

def ids( start, goal, depth=50 ):
	"""Perfoms an iterative depth first search."""
	for i in range( depth ):
		result = dls( start, goal, i )
		if result != None:
			return result



class Node:
	def __init__( self, state, parent, operator, depth, cost ):
		# Contains the state of the node
		self.state = state
		# Contains the node that generated this node
		self.parent = parent
		# Contains the operation that generated this node from the parent
		self.operator = operator
		# Contains the depth of this node (parent.depth +1)
		self.depth = depth
		# Contains the path cost of this node from depth 0. Not used for depth/breadth first.
		self.cost = cost
		# Contains the f-cost of this node from depth 0 for IDA_star search. 
		self.f_cost = 0
       
	 
	def getState(self):
		return self.state
		
	def getParent(self):
		return self.parent
		
	def getMoves(self):
		return self.operator
		
	def getCost(self):
		return self.cost
	
	def pathFromStart(self):
		stateList = []
		movesList = []
		currNode = self
		while currNode.getMoves() is not None:
			#print stateList
            #print movesList
			stateList.append(currNode.getState())
			movesList.append(currNode.getMoves())
			currNode = currNode.parent
		movesList.reverse()
		stateList.reverse()
		for state in stateList:
			display_board(state)
		return movesList
		
	 
# Main method
def main():
    #start_state=[1,3,4,8,6,2,7,0,5] [2,8,1,0,4,3,7,6,5] [5,6,7,4,0,8,3,2,1]
	start_state =[5,6,7,4,0,8,3,2,1]
	### CHANGE THIS FUNCTION TO USE bfs, dfs, dls, ids, greedy, a_star or ida_star
	start = time.clock() 
	result = ida_star( start_state, goal_state )
	end = time.clock() 
	totaltime= end-start
	if result == None:	
		print "No solution found"
	elif result == [None]: 
		print "Start node was the goal!"
	else:
		print result
		print len(result), " moves"
	print("Total searching time: %.5f seconds" % (totaltime))

# A python-isim. Basically if the file is being run execute the main() function.
if __name__ == "__main__":
	main()
