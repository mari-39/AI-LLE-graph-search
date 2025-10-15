from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from lle import World, Action, WorldState


S = TypeVar("S", bound=WorldState)


class SearchProblem(ABC, Generic[S]):
    """
    A Search Problem is a problem that can be solved by a search algorithm.

    The generic parameter S is the type of the problem state.
    """

    def __init__(self, world: World):
        self.world = world
        world.reset()
        self.initial_state = world.get_state()

    @abstractmethod
    def is_goal_state(self, problem_state: S) -> bool:
        """Whether the given state is the goal state"""

    def get_successors(self, state: S) -> list[tuple[WorldState, Action]]:
        """
        Returns  all possible states that can be reached from the given world state.

        Note that if an agent dies, the game is over and there is no successor to that state.
        """         
        # you get a WS e.g., WS { agents_positions: [(10, 9)], gems_collected: [true], agents_alive: [true] }
        # now you want [[WS0, North], [WS1, South], ...]

        # 1. load state into the world, but keep original world to restore later
        originalState = self.world.get_state()

        # 2. simulate all possible actions
        avActions = self.world.available_actions()[0]
        consequences = []
        print(avActions)

        # set world to given state
        self.world.set_state(state)

        # loop through list of actions, perform each one, store resulting state, then reset to given state
        for action in avActions:
            self.world.step([action]) # this changes self.world
            newState = self.world.get_state()

            if all(newState.agents_alive):
                consequences.append(newState)
                print(self.world.step(action))
            else:
                consequences.append(None)

            # reset to given state before performing next action in list
            self.world.set_state(state)

        # 3. return to original world, to avoid any real changes being made
        self.world.set_state(originalState)
        return list(zip(consequences, avActions))
        

    def heuristic(self, problem_state: S) -> float:
        raise NotImplementedError()
