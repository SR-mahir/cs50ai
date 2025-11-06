import sys

class Node():
    def __init__(self, state, parent,action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():   #this class or object works as frontier, nodes can be added or removed
    def __init__(self):
        self.frontier = []

    def add (self,node):
        self.frontier.append(node)    # stack data structure LIFO 

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)  # checks for particular state
    
    def empty(self):
        return len(self.frontier) == 0     #checks empty or not
    
    def remove(self):
        if self.empty:
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]  
            self.frontier = self.frontier[:-1]       # removes the last node (stack)
            return node
        

class QueueFrontier(StackFrontier):   #inherits the StackFrontier Class
    def remove(self):
        if self.empty:
            raise Exception("Empty frontier")
        else:
            node = self.frontier[0]  
            self.frontier = self.frontier[1:]       # removes the first node (stack)
            return node
        
# QueueFrontier for BFS and StackFrontier for DFS 

class Maze():
    def __init__(self,filename):
        with open(filename) as f:   #opening the file
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one end point")
        
        #height and width of maze
        contents = contents.splitlies()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        #walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start =(i,j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.start =(i,j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row-1, col)),
            ("down", (row+1, col)),
            ("left", (row, col-1)),
            ("right", (row, col+1)),
        ]
        result = []
        for action, (r,c) in candidates:
            if 0 <= r < self.height and 0 <= c <= self.width and not self.walls[r][c]:
                result.append(action, (r,c))
        
        return result
    
    def solve(self):
        """Finds a solution to maze if one exists."""

        