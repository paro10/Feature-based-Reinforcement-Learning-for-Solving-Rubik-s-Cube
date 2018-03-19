'''Rubik's Cube - MilestoneB.py
'''
#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Rubik's Cube"
PROBLEM_VERSION = "0.4"
PROBLEM_AUTHORS = ['Anirudh Rao', 'Paromita Banerjee']
PROBLEM_CREATION_DATE = "02-MARCH-2018"
PROBLEM_DESC=\
'''The following is the problem formulation of the Rubik's Cube puzzle,
which comprises of the state definition and valid move generator.
'''
#</METADATA>

# Each face is represented by a number
FACE1 = "TOP"
FACE2 = "LEFT"
FACE3 = "RIGHT"
FACE4 = "BOTTOM"
FACE5 = "BACK"
FACE6 = "FRONT"

FACE_LIST = [FACE1, FACE2, FACE3, FACE4, FACE5, FACE6]

LIVING_REWARD = -0.04

import copy

class State:
  def __init__(self, d):
    self.d = d

  def __eq__(self, s2):
    if not (type(self)==type(s2)): return False
    for f in [FACE1, FACE2, FACE3, FACE4, FACE5, FACE6]:
      if self.d[f] != s2.d[f]: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    # Each cube is represented as:
    #       BACK
    # LEFT  TOP   RIGHT  BOTTOM
    #       FRONT
    return self.print_face(FACE_LIST)

  def print_face(self, face_list):
    face1 = self.d[face_list[0]]
    face2 = self.d[face_list[1]]
    face3 = self.d[face_list[2]]
    face4 = self.d[face_list[3]]
    face5 = self.d[face_list[4]]
    face6 = self.d[face_list[5]]

    txt = "\n\n\t   ["
    txt += str(face5["q2"]) + "  " + str(face5["q1"])
    txt += "]\n"
    txt += "\t   [" + str(face5["q3"]) + "  " + str(face5["q4"]) + "]"

    txt += "\n\n"
    txt += "  [" + str(face2["q2"]) + "  " + str(face2["q1"]) + "]     [" + str(face1["q2"]) + "  " + str(face1["q1"]) + "]     [" +\
           str(face3["q2"]) + "  " + str(face3["q1"]) + "]     [" + str(face4["q2"]) + "  " + str(face4["q1"]) + "]"
    txt += "\n"    
    txt += "  [" + str(face2["q3"]) + "  " + str(face2["q4"]) + "]     [" + str(face1["q3"]) + "  " + str(face1["q4"]) + "]     [" + \
           str(face3["q3"]) + "  " + str(face3["q4"]) + "]     [" + str(face4["q3"]) + "  " + str(face4["q4"]) + "]"
    txt += "\n\n" 

    txt += "\t   ["
    txt += str(face6["q2"]) + "  " + str(face6["q1"])
    txt += "]\n"
    txt += "\t   [" + str(face6["q3"]) + "  " + str(face6["q4"]) + "]"

    return txt

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = copy.deepcopy(self)
    return news

  def can_move(self):
    '''Tests whether it's legal to move from one state to another. Since all moves are legal, always returns True'''
    return True
    
  def move(self, moveName):
    '''
    Assuming it's legal to make the move, this computes
    the new state resulting from moving from one state to another.
    '''
    news = self.copy()
    l1 = moveName.split("-")
    reference_face = l1[0]
    direction = l1[2]
    if reference_face == "front":
        #retrieving all existing values
        front_q1_value = self.d[FACE6]["q1"]
        front_q2_value = self.d[FACE6]["q2"]
        front_q3_value = self.d[FACE6]["q3"]
        front_q4_value = self.d[FACE6]["q4"]

        top_q3_value = self.d[FACE1]["q3"]
        top_q4_value = self.d[FACE1]["q4"]
        left_q3_value = self.d[FACE2]["q3"]
        left_q4_value = self.d[FACE2]["q4"]
        right_q3_value = self.d[FACE3]["q3"]
        right_q4_value = self.d[FACE3]["q4"]
        bottom_q3_value = self.d[FACE4]["q3"]
        bottom_q4_value = self.d[FACE4]["q4"]

        if direction == "right":
          #front face
          news.d[FACE6]["q1"] = front_q2_value
          news.d[FACE6]["q2"] = front_q3_value
          news.d[FACE6]["q3"] = front_q4_value
          news.d[FACE6]["q4"] = front_q1_value
          #top
          news.d[FACE1]["q3"] = left_q3_value
          news.d[FACE1]["q4"] = left_q4_value
          #left
          news.d[FACE2]["q3"] = bottom_q4_value
          news.d[FACE2]["q4"] = bottom_q3_value
          #right
          news.d[FACE3]["q3"] = top_q3_value
          news.d[FACE3]["q4"] = top_q4_value
          #bottom
          news.d[FACE4]["q3"] = right_q4_value
          news.d[FACE4]["q4"] = right_q3_value
        else:
          #front face
          news.d[FACE6]["q1"] = front_q4_value
          news.d[FACE6]["q2"] = front_q1_value
          news.d[FACE6]["q3"] = front_q2_value
          news.d[FACE6]["q4"] = front_q3_value
          #top
          news.d[FACE1]["q3"] = right_q3_value
          news.d[FACE1]["q4"] = right_q4_value
          #left
          news.d[FACE2]["q3"] = top_q3_value
          news.d[FACE2]["q4"] = top_q4_value
          #right
          news.d[FACE3]["q3"] = bottom_q4_value
          news.d[FACE3]["q4"] = bottom_q3_value
          #bottom
          news.d[FACE4]["q3"] = left_q4_value
          news.d[FACE4]["q4"] = left_q3_value

    if reference_face == "left":
        #retrieving all existing values
        left_q1_value = self.d[FACE2]["q1"]
        left_q2_value = self.d[FACE2]["q2"]
        left_q3_value = self.d[FACE2]["q3"]
        left_q4_value = self.d[FACE2]["q4"]

        top_q2_value = self.d[FACE1]["q2"]
        top_q3_value = self.d[FACE1]["q3"]
        bottom_q2_value = self.d[FACE4]["q2"]
        bottom_q3_value = self.d[FACE4]["q3"]
        back_q2_value = self.d[FACE5]["q2"]
        back_q3_value = self.d[FACE5]["q3"]
        front_q2_value = self.d[FACE6]["q2"]
        front_q3_value = self.d[FACE6]["q3"]

        if direction == "right":
          #LEFT
          news.d[FACE2]["q1"] = left_q2_value
          news.d[FACE2]["q2"] = left_q3_value
          news.d[FACE2]["q3"] = left_q4_value
          news.d[FACE2]["q4"] = left_q1_value
          #TOP
          news.d[FACE1]["q2"] = back_q2_value
          news.d[FACE1]["q3"] = back_q3_value
          #BOTTOM
          news.d[FACE4]["q2"] = front_q3_value
          news.d[FACE4]["q3"] = front_q2_value
          #BACK
          news.d[FACE5]["q2"] = bottom_q3_value
          news.d[FACE5]["q3"] = bottom_q2_value
          #FRONT
          news.d[FACE6]["q2"] = top_q2_value
          news.d[FACE6]["q3"] = top_q3_value
        else:
          #LEFT
          news.d[FACE2]["q1"] = left_q4_value
          news.d[FACE2]["q2"] = left_q1_value
          news.d[FACE2]["q3"] = left_q2_value
          news.d[FACE2]["q4"] = left_q3_value
          #TOP
          news.d[FACE1]["q2"] = front_q2_value
          news.d[FACE1]["q3"] = front_q3_value
          #BOTTOM
          news.d[FACE4]["q2"] = back_q3_value
          news.d[FACE4]["q3"] = back_q2_value
          #BACK
          news.d[FACE5]["q2"] = top_q2_value
          news.d[FACE5]["q3"] = top_q3_value
          #FRONT
          news.d[FACE6]["q2"] = bottom_q3_value
          news.d[FACE6]["q3"] = bottom_q2_value

    if reference_face == "right":
        #retrieving all existing values
        right_q1_value = self.d[FACE3]["q1"]
        right_q2_value = self.d[FACE3]["q2"]
        right_q3_value = self.d[FACE3]["q3"]
        right_q4_value = self.d[FACE3]["q4"]

        top_q1_value = self.d[FACE1]["q1"]
        top_q4_value = self.d[FACE1]["q4"]
        bottom_q1_value = self.d[FACE4]["q1"]
        bottom_q4_value = self.d[FACE4]["q4"]
        back_q1_value = self.d[FACE5]["q1"]
        back_q4_value = self.d[FACE5]["q4"]
        front_q1_value = self.d[FACE6]["q1"]
        front_q4_value = self.d[FACE6]["q4"]

        if direction == "right":
          #RIGHT
          news.d[FACE3]["q1"] = right_q2_value
          news.d[FACE3]["q2"] = right_q3_value
          news.d[FACE3]["q3"] = right_q4_value
          news.d[FACE3]["q4"] = right_q1_value
          #TOP
          news.d[FACE1]["q1"] = front_q1_value
          news.d[FACE1]["q4"] = front_q4_value
          #FRONT
          news.d[FACE6]["q1"] = bottom_q4_value
          news.d[FACE6]["q4"] = bottom_q1_value
          #BOTTOM
          news.d[FACE4]["q1"] = back_q4_value
          news.d[FACE4]["q4"] = back_q1_value
          #BACK
          news.d[FACE5]["q1"] = top_q1_value
          news.d[FACE5]["q4"] = top_q4_value
        else:
          #RIGHT
          news.d[FACE3]["q1"] = right_q4_value
          news.d[FACE3]["q2"] = right_q1_value
          news.d[FACE3]["q3"] = right_q2_value
          news.d[FACE3]["q4"] = right_q3_value
          #TOP
          news.d[FACE1]["q1"] = back_q1_value
          news.d[FACE1]["q4"] = back_q4_value
          #FRONT
          news.d[FACE6]["q1"] = top_q1_value
          news.d[FACE6]["q4"] = top_q4_value
          #BOTTOM
          news.d[FACE4]["q1"] = front_q4_value
          news.d[FACE4]["q4"] = front_q1_value
          #BACK
          news.d[FACE5]["q1"] = bottom_q4_value
          news.d[FACE5]["q4"] = bottom_q1_value

    if reference_face=='top':
        #retrieving all existing values
        top_q1_value=self.d[FACE1]["q1"]
        top_q2_value=self.d[FACE1]["q2"]
        top_q3_value=self.d[FACE1]["q3"]
        top_q4_value=self.d[FACE1]["q4"]

        left_q1_value=self.d[FACE2]["q1"]
        left_q4_value=self.d[FACE2]["q4"]
        right_q2_value=self.d[FACE3]["q2"]
        right_q3_value=self.d[FACE3]["q3"]
        front_q1_value=self.d[FACE6]["q1"]
        front_q2_value=self.d[FACE6]["q2"]
        back_q3_value=self.d[FACE5]["q3"]
        back_q4_value=self.d[FACE5]["q4"]

        if direction=='right':
          #updating top face:
          news.d[FACE1]["q1"]=top_q2_value
          news.d[FACE1]["q2"]=top_q3_value
          news.d[FACE1]["q3"]=top_q4_value
          news.d[FACE1]["q4"]=top_q1_value

          #updating left face:
          news.d[FACE2]["q1"]=front_q2_value
          news.d[FACE2]["q4"]=front_q1_value
          #updating right face:
          news.d[FACE3]["q2"]=back_q3_value
          news.d[FACE3]["q3"]=back_q4_value
          #updating front face:
          news.d[FACE6]["q1"]=right_q2_value
          news.d[FACE6]["q2"]=right_q3_value
          #updating back face:
          news.d[FACE5]["q3"]=left_q4_value
          news.d[FACE5]["q4"]=left_q1_value

        if direction=='left':
          #updating top face:
          news.d[FACE1]["q1"]=top_q4_value
          news.d[FACE1]["q2"]=top_q1_value
          news.d[FACE1]["q3"]=top_q2_value
          news.d[FACE1]["q4"]=top_q3_value

          #updating left face:
          news.d[FACE2]["q1"]=back_q4_value
          news.d[FACE2]["q4"]=back_q3_value
          #updating right face:
          news.d[FACE3]["q2"]=front_q1_value
          news.d[FACE3]["q3"]=front_q2_value
          #updating front face:
          news.d[FACE6]["q1"]=left_q4_value
          news.d[FACE6]["q2"]=left_q1_value
          #updating back face:
          news.d[FACE5]["q3"]=right_q2_value
          news.d[FACE5]["q4"]=right_q3_value

    if reference_face=='back':
        #retrieving all existing values
        back_q1_value=self.d[FACE5]["q1"]
        back_q2_value=self.d[FACE5]["q2"]
        back_q3_value=self.d[FACE5]["q3"]
        back_q4_value=self.d[FACE5]["q4"]

        left_q1_value=self.d[FACE2]["q1"]
        left_q2_value=self.d[FACE2]["q2"]
        right_q1_value=self.d[FACE3]["q1"]
        right_q2_value=self.d[FACE3]["q2"]
        top_q1_value=self.d[FACE1]["q1"]
        top_q2_value=self.d[FACE1]["q2"]
        bottom_q1_value=self.d[FACE4]["q1"]
        bottom_q2_value=self.d[FACE4]["q2"]

        if direction=='right':
          #updating back face:
          news.d[FACE5]["q1"]=back_q2_value
          news.d[FACE5]["q2"]=back_q3_value
          news.d[FACE5]["q3"]=back_q4_value
          news.d[FACE5]["q4"]=back_q1_value

          #updating left face:
          news.d[FACE2]["q1"]=top_q1_value
          news.d[FACE2]["q2"]=top_q2_value
          #updating right face:
          news.d[FACE3]["q1"]=bottom_q2_value
          news.d[FACE3]["q2"]=bottom_q1_value
          #updating bottom face:
          news.d[FACE4]["q1"]=left_q2_value
          news.d[FACE4]["q2"]=left_q1_value
          #updating top face:
          news.d[FACE1]["q1"]=right_q1_value
          news.d[FACE1]["q2"]=right_q2_value

        if direction=='left':
          #updating back face:
          news.d[FACE5]["q1"]=back_q4_value
          news.d[FACE5]["q2"]=back_q1_value
          news.d[FACE5]["q3"]=back_q2_value
          news.d[FACE5]["q4"]=back_q3_value

          #updating left face:
          news.d[FACE2]["q1"]=bottom_q2_value
          news.d[FACE2]["q2"]=bottom_q1_value
          #updating right face:
          news.d[FACE3]["q1"]=top_q1_value
          news.d[FACE3]["q2"]=top_q2_value
          #updating bottom face:
          news.d[FACE4]["q1"]=right_q2_value
          news.d[FACE4]["q2"]=right_q1_value
          #updating top face:
          news.d[FACE1]["q1"]=left_q1_value
          news.d[FACE1]["q2"]=left_q2_value


    if reference_face=='bottom':
        #retrieving all values
        bottom_q1_value=self.d[FACE4]["q1"]
        bottom_q2_value=self.d[FACE4]["q2"]
        bottom_q3_value=self.d[FACE4]["q3"]
        bottom_q4_value=self.d[FACE4]["q4"]

        left_q2_value=self.d[FACE2]["q2"]
        left_q3_value=self.d[FACE2]["q3"]
        right_q1_value=self.d[FACE3]["q1"]
        right_q4_value=self.d[FACE3]["q4"]
        front_q3_value=self.d[FACE6]["q3"]
        front_q4_value=self.d[FACE6]["q4"]
        back_q1_value=self.d[FACE5]["q1"]
        back_q2_value=self.d[FACE5]["q2"]

        if direction=='right':
          #updating bottom face:
          news.d[FACE4]["q1"]=bottom_q4_value
          news.d[FACE4]["q2"]=bottom_q1_value
          news.d[FACE4]["q3"]=bottom_q2_value
          news.d[FACE4]["q4"]=bottom_q3_value

          #updating left face:
          news.d[FACE2]["q2"]=back_q1_value
          news.d[FACE2]["q3"]=back_q2_value
          #updating right face:
          news.d[FACE3]["q1"]=front_q4_value
          news.d[FACE3]["q4"]=front_q3_value
          #updating front face:
          news.d[FACE6]["q3"]=left_q2_value
          news.d[FACE6]["q4"]=left_q3_value
          #updating back face:
          news.d[FACE5]["q1"]=right_q4_value
          news.d[FACE5]["q2"]=right_q1_value

        if direction=='left':
          #updating bottom face:
          news.d[FACE4]["q1"]=bottom_q2_value
          news.d[FACE4]["q2"]=bottom_q3_value
          news.d[FACE4]["q3"]=bottom_q4_value
          news.d[FACE4]["q4"]=bottom_q1_value

          #updating left face:
          news.d[FACE2]["q2"]=front_q3_value
          news.d[FACE2]["q3"]=front_q4_value
          #updating right face:
          news.d[FACE3]["q1"]=back_q2_value
          news.d[FACE3]["q4"]=back_q1_value
          #updating front face:
          news.d[FACE6]["q3"]=right_q4_value
          news.d[FACE6]["q4"]=right_q1_value
          #updating back face:
          news.d[FACE5]["q1"]=left_q2_value
          news.d[FACE5]["q2"]=left_q3_value

    return news # return new state


# Transition probability
def T(s, a, sp):
    '''Compute the transition probability for going from state s to
       state sp after taking action a.'''
    return 1


def R(s, a, sp):
  '''
  If the transition from the exising goal state leads to a goal state
  return a reward of +100. Otherwise return a living reward of -0.04
  '''
  # Handle goal state transitions first...
  if goalStateCheck(sp):
    return 100.0    
  # Handle all other transitions:
  return LIVING_REWARD


'''
Check for all possible goal states. 
A goal state looked from any orientation is a goal state, i.e., 
a rotated cube which is at the goal state.
'''
def goalStateCheck(s):
    for side, value1 in s.d.items():
      value_list = []
      for k,v in value1.items():
        value_list.append(v)
      if len(set(value_list))>1:
        return False
    return True


def goal_test(s):
  '''Checks for Goal state  '''
  goalStateCheck(s)


def goal_message(s):
  return "Rubik's Cube has been solved!"


class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

#</COMMON_CODE>


#Check how many faces are complete
def getCompleteFacesCount(s):
  complete_faces = 0
  for i in range(len(FACE_LIST)):
      face_vals = s.d[FACE_LIST[i]]
      if face_vals["q1"] == face_vals["q2"] == face_vals["q4"] == face_vals["q4"]:
        complete_faces+=1

  return complete_faces


# Total number of squares at the right faces in the cube
def one_side(s):
  m = 0
  for i in range(len(FACE_LIST)):
    value = i + 1
    face = s.d[FACE_LIST[i]]
    count = 0
    for k, v in face.items():
      if v == value:
        count += 1
    if count > m: m = count
  return m


GOAL_STATE = State({
                FACE1 : {"q1" : 1, "q2" : 1, "q3" : 1, "q4" : 1}, #TOP
                FACE2 : {"q1" : 2, "q2" : 2, "q3" : 2, "q4" : 2}, #LEFT
                FACE3 : {"q1" : 3, "q2" : 3, "q3" : 3, "q4" : 3}, #RIGHT
                FACE4 : {"q1" : 4, "q2" : 4, "q3" : 4, "q4" : 4}, #BOTTOM
                FACE5 : {"q1" : 5, "q2" : 5, "q3" : 5, "q4" : 5}, #BACK
                FACE6 : {"q1" : 6, "q2" : 6, "q3" : 6, "q4" : 6}  #FRONT
                })

#</INITIAL STATE>

# not using
TERMINAL_STATE = State({
                FACE1 : {"q0" : 0, "q0" : 0, "q0" : 0, "q0" : 0}, #TOP
                FACE2 : {"q0" : 0, "q0" : 0, "q0" : 0, "q0" : 0}, #LEFT
                FACE3 : {"q0" : 0, "q0" : 0, "q0" : 0, "q0" : 0}, #RIGHT
                FACE4 : {"q0" : 0, "q0" : 0, "q0" : 0, "q0" : 0}, #BOTTOM
                FACE5 : {"q0" : 0, "q0" : 0, "q0" : 0, "q0" : 0}, #BACK
                FACE6 : {"q0" : 0, "q0" : 0, "q0" : 0, "q0" : 0}  #FRONT
                })


def CREATE_INITIAL_STATE():
  return State({
                FACE1 : {"q1" : 1, "q2" : 1, "q3" : 1, "q4" : 1}, #TOP
                FACE2 : {"q1" : 5, "q2" : 2, "q3" : 2, "q4" : 5}, #LEFT
                FACE3 : {"q1" : 3, "q2" : 6, "q3" : 6, "q4" : 3}, #RIGHT
                FACE4 : {"q1" : 4, "q2" : 4, "q3" : 4, "q4" : 4}, #BOTTOM
                FACE5 : {"q1" : 5, "q2" : 5, "q3" : 3, "q4" : 3}, #BACK
                FACE6 : {"q1" : 2, "q2" : 2, "q3" : 6, "q4" : 6}  #FRONT
                })

#</INITIAL_STATE>
INITIAL_STATE = CREATE_INITIAL_STATE()

# Allowed actions
ACTIONS = ['front-face-right', 'back-face-right', 'left-face-right', 'right-face-right', \
          'top-face-right', 'bottom-face-right',\
          'front-face-left', 'back-face-left', \
          'left-face-left', 'right-face-left', 'top-face-left', 'bottom-face-left'] 

#<OPERATORS>
OPERATORS = [Operator(move,
                      lambda s: s.can_move(),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s, a1=move: s.move(a1))
             for move in ACTIONS]
#</OPERATORS>

# Create a dictionary mapping of each action to its operator
action_to_operator_dict = {}
for a in ACTIONS:
  action_to_operator_dict[a] = Operator(a, lambda s: s.can_move(), lambda s, a1=a: s.move(a1))

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)

GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
