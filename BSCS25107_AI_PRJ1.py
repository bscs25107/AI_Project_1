""" QUESTION NO. 2 [ BFS] """
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
