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
        manhattanDist = 0

        def distanceToExit(agentPosn: tuple[int, int], exitPosn: tuple[int, int]) -> int:
            d_x = abs(agentPosn[0] - exitPosn[0])
            d_y = abs(agentPosn[1] - exitPosn[1])
            return d_x + d_y

        for agentPosn in agentPosnList:
            min_d_to_exit = min([distanceToExit(agentPosn, exitPosn) for exitPosn in exitPosnList])
            manhattanDist += min_d_to_exit

        # prettier: return sum(min(distanceToExit(agentPosn, exitPosn) for exitPosn in exitPosnList) for agentPosn in agentPosnList)
        return manhattanDist          
        

        