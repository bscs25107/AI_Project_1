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
