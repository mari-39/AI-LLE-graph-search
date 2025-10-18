from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from lle import Action, WorldState

from priority_queue import PriorityQueue
from problem import SearchProblem

S = TypeVar("S", bound=WorldState)


@dataclass
class Solution(Generic[S]):
    actions: list[Action]
    states: list[S]

    @property
    def n_steps(self) -> int:
        return len(self.actions)

    @staticmethod
    def from_node(node: "SearchNode") -> "Solution[S]":
        actions = []
        states = []
        while node.parent is not None:
            actions.append(node.prev_action)
            states.append(node.state)
            node = node.parent
        actions.reverse()
        return Solution(actions, states)


@dataclass
class SearchNode:
    state: WorldState
    parent: Optional["SearchNode"]
    prev_action: Optional[Action]
    cost: float = 0.0

    def __hash__(self) -> int:
        return hash((self.state, self.cost))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SearchNode):
            return NotImplemented
        return self.state == other.state and self.cost == other.cost


def dfs(problem: SearchProblem) -> Optional[Solution]:
    raise NotImplementedError()


def bfs(problem: SearchProblem) -> Optional[Solution]:
    queue = PriorityQueue()
    initialState = problem.initial_state # first State of (sub)-tree
    #print("intialState: ", initialState)
    root = SearchNode(initialState, None, None)
    visitedStates = set()
    

    queue.push(root, queue.count)
    visitedStates.add(root)

    while not(queue.is_empty()):
        parentNode = queue.pop()
        #print("chosen node: ", parentNode)
        parentState = parentNode.state

        if problem.is_goal_state(parentState):
            return Solution.from_node(parentNode)

        childrenStates = problem.get_successors(parentState) # gets next layer

        for child in childrenStates:
            queue.count += 1
            childNode = SearchNode(child[0], parentNode, child[1])
            #print("updated Prio: ", queue.count)
            if not(childNode in visitedStates):
                queue.push(childNode, queue.count)
                visitedStates.add(childNode)
    return None


def astar(problem: SearchProblem) -> Optional[Solution]:
    raise NotImplementedError()
