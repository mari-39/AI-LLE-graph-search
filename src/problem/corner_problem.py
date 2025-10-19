from lle import WorldState, World
from .problem import SearchProblem


class CornerState(WorldState): ...


class CornerProblem(SearchProblem[CornerState]):
    def __init__(self, world: World):
        super().__init__(world)
        self.corners = [(0, 0), (0, world.width - 1), (world.height - 1, 0), (world.height - 1, world.width - 1)]
        # self.initial_state = CornerState(...)

    def is_goal_state(self, state: CornerState) -> bool:
        raise NotImplementedError

    def get_successors(self, state: CornerState):
        successors = []
        for world_state, actions in super().get_successors(state):
            # You probably need to do something like this here
            # next_state = CornerState(...)
            raise NotImplementedError()
        return successors

    def heuristic(self, problem_state: WorldState) -> float:
        height = self.world.height
        width = self.world.width

        agentPosnList = problem_state.agents_positions
        exitPosnList = self.world.exit_pos
        cornerPosnList = [[0, 0], [0, height], [width, 0], [width, height]]
        
        return 0.0