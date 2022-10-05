# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    from game import Directions

    if(problem.isGoalState(problem.getStartState())):
        return problem.getStartState()

    act = problem.getStartState() # Devuelve la coordenada inicial
    stack = util.Stack()
    stack.push(act)
    vistos = []
    caminos = {}
    camino_final = []

    while not stack.isEmpty():
        act = stack.pop()

        if act not in vistos:
            vistos.append(act) # Lo marco como visto
            if problem.isGoalState(act):              
                camino_final = caminos.get(act)
                print(camino_final)
                return camino_final

            for sucesor in problem.getSuccessors(act):
                stack.push(sucesor[0])
                # Caso Critico: Primer estado que no tiene camino todavia
                if caminos.get(act) == None:
                    caminos[sucesor[0]] = [] + [sucesor[1]]
                # Caso General: Voy acumulando el camino
                else:
                    caminos[sucesor[0]] = caminos.get(act) + [sucesor[1]]
    
    return False



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    if(problem.isGoalState(problem.getStartState())):
        return problem.getStartState()

    act = problem.getStartState() # Devuelve la coordenada inicial
    cola = util.Queue()
    cola.push(act)
    vistos = []
    caminos = {}

    while not cola.isEmpty():
        act = cola.pop()
        if act not in vistos:
            vistos.append(act) # Lo marco como visto
            if problem.isGoalState(act):              
                return caminos.get(act)

            for sucesor in problem.getSuccessors(act):
                cola.push(sucesor[0])
                # Caso Critico: Primer estado que no tiene camino todavia
                if caminos.get(act) == None:
                    caminos[sucesor[0]] = [] + [sucesor[1]]

                # Caso General: Voy acumulando el camino
                else:
                    # Para conseguir el camino más corto voy mejorando el camino a seguir para llegar a un estado
                    # Si el sucesor ya esta en caminos ya he trazado un camino hacia el
                    if sucesor[0] in caminos:
                        # Si el camino ya trazado es es mayor que el camino de act + 1 se puede mejorar trazando desde act
                        if len(caminos.get(act)) + 1 < len(caminos.get(sucesor[0])):
                            # Se acumula el camino
                            
                            caminos[sucesor[0]] = caminos.get(act) + [sucesor[1]]

                        # Si no se puede mejorar, no se cambia
                    else:
                        caminos[sucesor[0]] = caminos.get(act) + [sucesor[1]]
    print(caminos)
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    act = problem.getStartState() # Devuelve la coordenada inicial (coord)
    cola = util.PriorityQueue()
    cola.update(act, 0)

    vistos = []
    # Cada key de caminos tiene [camino, coste]
    caminos = {act: [None, 0]}

    while not cola.isEmpty():
        act = cola.pop()
        camino_act = caminos.get(act)[0]
        coste_act = caminos.get(act)[1]
        
        if act not in vistos:
            vistos.append(act)
            if problem.isGoalState(act):
                return caminos.get(act)[0]
            
            for s in problem.getSuccessors(act):
                # Si ya lo he añadido a caminos puedo optimizarlo o no              
                camino_s = [s[1]]
                coste_acum = coste_act + s[2]
                
                if camino_act == None:
                    caminos[s[0]] = [] + camino_s, coste_acum
                    cola.update(s[0], coste_acum)
                else:
                    if s[0] in caminos:
                        if coste_acum < caminos.get(s[0])[1]:
                            # Reemplazo
                            caminos[s[0]] = camino_act + camino_s, coste_acum
                            cola.update(s[0], coste_acum)
                    else:
                        caminos[s[0]] = camino_act + camino_s, coste_acum
                        cola.update(s[0], coste_acum)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    act = problem.getStartState()
    cola = util.PriorityQueue()

    # Meto en la cola el primero junto con la prioridad calculada con el heuristico
    cola.update(act, heuristic(act, problem))
    vistos = []
    # Cada key de caminos tiene [camino, coste]
    caminos = {act: [None, heuristic(act, problem)]}
    
    while not cola.isEmpty():
        act = cola.pop()
        camino_act = caminos.get(act)[0]
        coste_act = caminos.get(act)[1]

        if act not in vistos:
            vistos.append(act)
            if problem.isGoalState(act):
                return caminos.get(act)[0]

            for s in problem.getSuccessors(act):
                camino_s = [s[1]]
                coste_acum = coste_act + heuristic(s[0], problem) + s[2]

                if camino_act == None:
                    caminos[s[0]] = [] + camino_s, coste_acum
                    cola.update(s[0], coste_acum)
                else:
                    if s[0] in caminos:
                        if coste_acum < caminos.get(s[0])[1]:
                            # Reemplazo
                            caminos[s[0]] = camino_act + camino_s, coste_acum
                            cola.update(s[0], coste_acum)
                    else:
                        caminos[s[0]] = camino_act + camino_s, coste_acum
                        cola.update(s[0], coste_acum)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
