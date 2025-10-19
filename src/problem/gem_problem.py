from lle import WorldState
from .problem import SearchProblem


class GemProblem(SearchProblem[WorldState]):
    # first collect all gems
    # then reach exit
    def is_goal_state(self, state: WorldState) -> bool:
        raise NotImplementedError()

    def heuristic(self, problem_state: WorldState) -> float:
        agentPosnList = problem_state.agents_positions
        exitPosnList = self.world.exit_pos
        gemPosnList = [gem.pos for gem in self.world.gems]
        
        def distance(agentPosn: tuple[int, int], goal: tuple[int, int]) -> int:
            d_x = abs(agentPosn[0] - goal[0])
            d_y = abs(agentPosn[1] - goal[1])
            return d_x + d_y
        
        if (not(all(problem_state.gems_collected))):
            return sum(min(distance(agentPosn, gemPosn) for gemPosn in gemPosnList) for agentPosn in agentPosnList)
        else:
            return sum(min(distance(agentPosn, exitPosn) for exitPosn in exitPosnList) for agentPosn in agentPosnList)
