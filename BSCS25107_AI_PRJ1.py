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
