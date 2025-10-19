from lle import WorldState
from .problem import SearchProblem


class ExitProblem(SearchProblem[WorldState]):
    """
    A simple search problem where the agents must reach the exit **alive**.
    """
    # all agents alive + all agents at an exit

    def is_goal_state(self, problem_state: WorldState) -> bool:
        if all(problem_state.agents_alive):
            agentPosnList = problem_state.agents_positions
            exitPosnList = self.world.exit_pos

            for agentPosn in agentPosnList:
                if agentPosn in exitPosnList:
                    continue
                else:
                    return False
                
            return True
        else:
            return False
        
    def heuristic(self, problem_state: WorldState) -> float: # this never overstimates, as this is the minimum of moves needed
        agentPosnList = problem_state.agents_positions
        exitPosnList = self.world.exit_pos
        return max(min(self.manhattanDist(agentPosn, exitPosn) for exitPosn in exitPosnList) for agentPosn in agentPosnList)
        

        