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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    dir = {problem.getStartState(): None}
    stack = util.Stack()
    lista = []
    stack.push(problem.getStartState())

    while not stack.isEmpty():
        state = stack.pop()
        if problem.isGoalState(state):
            return list(dir[state])
        if state not in lista:
            lista.append(state)
            for s in problem.getSuccessors(state):
                if dir[state] is None:
                    dir[s[0]] = [s[1]]
                else:
                    n_dic = dir[state].copy()
                    n_dic.append(s[1])
                    dir[s[0]] = n_dic
                stack.push(s[0])
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""


    dir = {problem.getStartState(): None}
    queue = util.Queue()
    lista = []
    queue.push(problem.getStartState())

    while not queue.isEmpty():
        state = queue.pop()
        if problem.isGoalState(state):
            print(state)
            return list(dir[state])
        if state not in lista:
            lista.append(state)
            for s in problem.getSuccessors(state):
                if dir[state] is None:
                    dir[s[0]] = [s[1]]
                elif s[0] in dir and dir[s[0]] is not None:
                    if len(dir[state]) < len(dir[s[0]]):
                        n_dic1 = dir[state].copy()
                        n_dic1.append(s[1])
                        dir[s[0]] = n_dic1
                else:
                    n_dic1 = dir[state].copy()
                    n_dic1.append(s[1])

                    dir[s[0]] = n_dic1

                queue.push(s[0])
    return []


    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    dir = {problem.getStartState(): [None, 0]}
    queue = util.PriorityQueue()
    lista = []
    queue.push(problem.getStartState(), 0)

    while not queue.isEmpty():
        state = queue.pop()
        if problem.isGoalState(state):
            return list(dir[state][0])
        if state not in lista:
            lista.append(state)
            for s in problem.getSuccessors(state):
                if dir[state][0] is None:
                    dir[s[0]] = [[s[1]], s[2]]
                    prio = s[2]
                elif s[0] in dir and dir[s[0]] is not None:
                    if dir[state][1] + s[2] < dir[s[0]][1]:
                        n_dic1 = dir[state][0].copy()
                        n_dic2 = dir[state][1]
                        n_dic1.append(s[1])
                        n_dic2 += s[2]
                        dir[s[0]] = [n_dic1, n_dic2]
                        prio = n_dic2
                else:
                    n_dic1 = dir[state][0].copy()
                    n_dic2 = dir[state][1]
                    n_dic1.append(s[1])
                    n_dic2 += s[2]
                    dir[s[0]] = [n_dic1, n_dic2]
                    prio = n_dic2

                queue.push(s[0], prio)


    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    dir = {problem.getStartState(): [None, 0]}
    queue = util.PriorityQueue()
    lista = []
    queue.push(problem.getStartState(), 0)

    while not queue.isEmpty():
        state = queue.pop()
        if problem.isGoalState(state):
            return list(dir[state][0])
        if state not in lista:
            lista.append(state)
            for s in problem.getSuccessors(state):
                if dir[state][0] is None:
                    dir[s[0]] = [[s[1]], s[2]]
                    prio = s[2] + heuristic(s[0], problem)
                    queue.push(s[0], prio)
                elif s[0] in dir and dir[s[0]] is not None:
                    if dir[state][1] + s[2] < dir[s[0]][1]:
                        n_dic1 = dir[state][0].copy()
                        n_dic2 = dir[state][1]
                        n_dic1.append(s[1])
                        n_dic2 += s[2]
                        dir[s[0]] = [n_dic1, n_dic2]
                        prio = n_dic2 + heuristic(s[0], problem)
                        queue.update(s[0], prio)
                else:
                    n_dic1 = dir[state][0].copy()
                    n_dic2 = dir[state][1]
                    n_dic1.append(s[1])
                    n_dic2 += s[2]
                    dir[s[0]] = [n_dic1, n_dic2]
                    prio = n_dic2 + heuristic(s[0], problem)
                    queue.push(s[0], prio)




    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
