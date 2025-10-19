from lle import WorldState
from .problem import SearchProblem


class GemProblem(SearchProblem[WorldState]):
    # first collect all gems
    # then reach exit
    def is_goal_state(self, state: WorldState) -> bool:
        # if all gems collected + all agents in exit posn
        raise NotImplementedError()

    def heuristic(self, problem_state: WorldState) -> float:
        agentPosnList = problem_state.agents_positions
        exitPosnList = self.world.exit_pos
        gemPosnList = [gem.pos 
            for gem, collected_status in zip(self.world.gems, problem_state.gems_collected) 
            if not collected_status]
        
        if (not(all(problem_state.gems_collected))):
            min_dist_collection = min(self.distance(agentPosn, gemPosn) # COST OF ONE GEM COLLECTION / START: we need to collect min. 1 gem, make it the cheapest
                                    for agentPosn in agentPosnList
                                    for gemPosn in gemPosnList)
            
            min_dist_gem_exit = min(self.distance(gemPosn, exitPosn) # COST OF EXIT: we end up at a gem and look at the best-case distance of the last gem to the nearest exit 
                for exitPosn in exitPosnList 
                for gemPosn in gemPosnList)
        
            return  min_dist_collection + min_dist_gem_exit
        
        else:
            return sum(min(self.distance(agentPosn, exitPosn) for exitPosn in exitPosnList) for agentPosn in agentPosnList)
