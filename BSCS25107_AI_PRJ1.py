""" QUESTION NO. 2 [ BFS ] """
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first (graph search)."""
   
  fringe = Queue()
    expanded = set()

    fringe.push((problem.getStartState(), []))

    while not fringe.isEmpty():
        state, actions = fringe.pop()

        if problem.isGoalState(state):
            return actions

        if state not in expanded:
            expanded.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                fringe.push((successor, actions + [action]))
              
    return None

""" QUESTION NO. 4 [ IDS ] """
def iterativeDeepeningSearch(problem, maxDepth=10000):
    """
    Run depthLimitedSearch with limit = 0, 1, 2, ... until it finds a
    solution. Return that solution, or None if the problem has no solution
    (or none within maxDepth).
    """
   
    for limit in range(maxDepth):          
        result = depthLimitedSearch(problem, limit)
        if result is not CUTOFF:         
            return result
    return None

""" QUESTION NO. 6 [ GBFS ] """
def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that SEEMS closest to the goal first, i.e. the one with
    the lowest heuristic(state, problem) value (graph search).
    """
    fringe = PriorityQueue()
    expanded = set()

    start = problem.getStartState()
    fringe.push((start, []), heuristic(start, problem))

    while not fringe.isEmpty():
        state, actions = fringe.pop()

        if problem.isGoalState(state):
            return actions

        if state not in expanded:
            expanded.add(state)
            for succ, action, cost in problem.getSuccessors(state):
                fringe.push((succ, actions + [action]), heuristic(succ, problem))
    return None

""" -------------------------------------- """

def manhattanHeuristic(state, problem):
    """
    Q6: the Manhattan distance from 'state' to problem.goal:
        |row1 - row2| + |col1 - col2|
    """
    goal = problem.goal
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def euclideanHeuristic(state, problem):
    """
    Q6: the straight-line (Euclidean) distance from 'state' to problem.goal.
    """
   
    goal = problem.goal
    return math.sqrt((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2)
    util.raiseNotDefined()

""" QUESTION NO. 8 [ The Griever Hole ] """
class KeyHuntProblem(SearchProblem):
    """
    Q8: Collect every code piece, then reach the exit.

    You choose the state representation, with two requirements:
      1. A state must be HASHABLE (tuples, frozensets, ints, strings... but
         not lists, sets or dicts), because your search keeps them in sets.
      2. A state must be a TUPLE whose FIRST element is Thomas's (row, col)
         position. The display and the grader read state[0].

    Keep the state small: store only what you need to know to decide what
    happens next. Do NOT put the whole maze in the state.
    """

    def __init__(self, maze):
        self.maze = maze
        self.startPosition = maze.start
        self.keys = tuple(maze.keys)      # positions of all code pieces
        self.exit = maze.exit
        self.heuristicInfo = {}           # scratch space for your heuristic
        # Bookkeeping for the display and the grader. Do not touch.
        self._expanded = 0
        self._expandedOrder = []
        "*** YOUR CODE HERE (optional: set up anything else you need) ***"

    def getStartState(self):
        """Returns the start state, a tuple (startPosition, ...)."""
        return (self.startPosition, frozenset())

    def isGoalState(self, state):
        """True when every code piece has been collected AND Thomas is at the exit."""
        position, collected = state
        return position == self.exit and len(collected) == len(self.keys)

    def getSuccessors(self, state):
        """
        Returns a list of (successor, action, stepCost) triples.

        Use self.maze.neighbors(position), which gives the legal
        (action, nextPosition) pairs in North, South, East, West order, and
        self.maze.cost(nextPosition) for the step cost.
        """
        # Bookkeeping. Keep these two lines.
        self._expanded += 1
        self._expandedOrder.append(state[0])

        successors = []
        position, collected = state
        for action, nextPos in self.maze.neighbors(position):
            cost = self.maze.cost(nextPos)
            if nextPos in self.keys:
                newCollected = collected | {nextPos}
            else:
                newCollected = collected
            successors.append(((nextPos, newCollected), action, cost))
        return successors
