#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Rubik's Cube"
PROBLEM_VERSION = "0.4"
PROBLEM_AUTHORS = ['Anirudh Rao', 'Paromita Banerjee']
PROBLEM_CREATION_DATE = "06-MARCH-2018"
PROBLEM_DESC=\
'''
The following file needs to be run to start the agent. 
To run this file, type the following command at the terminal:

>> python Run.py

The user is presented a fully solved Rubik's cube and asked to enter
the number of times it needs to be shuffled to define the start state.

'''
#</METADATA>


import Cube_State as Cubes, MDP, sys, random

def test():

    initial_state = Cubes.GOAL_STATE
    action_ops = Cubes.action_to_operator_dict
    print("The goal state is :\n")

    print(initial_state, "\n")

    number_of_shuffles = input("Enter the number of times you want to shuffle the solved Rubik's cube: ")
    for i in number_of_shuffles:
        action = random.choice(Cubes.ACTIONS)
        initial_state = action_ops[action].state_transf(initial_state)

    print("The new initial state is :\n")
    print(initial_state, "\n")

    # Initialize MDP and initialize the appropriate class variables.
    rubik_MDP = MDP.MDP()
    rubik_MDP.register_start_state(initial_state)
    rubik_MDP.register_actions(Cubes.ACTIONS)
    rubik_MDP.register_operators(Cubes.OPERATORS)
    rubik_MDP.register_reward_function(Cubes.R)
    rubik_MDP.register_goal_state(Cubes.GOAL_STATE)
    rubik_MDP.register_goal_state_check(Cubes.goalStateCheck)
    rubik_MDP.register_features([Cubes.one_side, Cubes.getCompleteFacesCount]) #TODO Corners complete
    rubik_MDP.register_action_to_op(Cubes.action_to_operator_dict)
    rubik_MDP.register_weights([0, 0])
    print("========= SARSA LEARNING =======")
    rubik_MDP.sarsaLearning(0.9, 100, 0.2, 0.05) #discount, episodes, epsilon, learning_rate

    
test()