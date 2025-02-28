import sys

row_1 = input()
row_2 = input()
row_3 = input()
all_buttons_pressed = input()

# Store the grid
states = dict()
states[1] = row_1[0]
states[2] = row_1[2]
states[3] = row_1[4]
states[4] = row_2[0]
states[5] = row_2[2]
states[6] = row_2[4]
states[7] = row_3[0]
states[8] = row_3[2]
states[9] = row_3[4]

# Return reverse state
def reverse_state(state):
    return "~" if state == "*" else "*"

# Updates the grid according to the number of the button that was pressed
def update_states(button_nr):

  to_be_updated = ()

  if button_nr == 1:
    to_be_updated = (1,2,4,5)
  elif button_nr == 2:
    to_be_updated = (1,2,3)
  elif button_nr == 3:
    to_be_updated = (2,3,5,6)
  elif button_nr == 4:
    to_be_updated = (1,4,7)
  elif button_nr == 5:
    to_be_updated = (2,4,5,6,8)
  elif button_nr == 6:
    to_be_updated = (3,6,9)
  elif button_nr == 7:
    to_be_updated = (4,5,7,8)
  elif button_nr == 8:
    to_be_updated = (7,8,9)
  elif button_nr == 9:
    to_be_updated = (5,6,8,9)
    
  for i in to_be_updated:
    states[i] = reverse_state(states[i])

# Process the buttons pressed by the user
for i in range(0, len(all_buttons_pressed)):
    button_nr = int(all_buttons_pressed[i])
    update_states(button_nr)

# Find the number that needs to be pressed
answer = -1
if states[1] == "~" and states[2] == "~" and states[4] == "~" and states[5] == "*":
    answer = 1
elif states[1] == "~" and states[2] == "~" and states[3] == "~" :
    answer = 2
elif states[2] == "~" and states[3] == "~" and states[5] == "*" and states[6] == "~":
    answer = 3
elif states[1] == "~" and states[4] == "~" and states[7] == "~" :
    answer = 4
elif states[2] == "~" and states[5] == "*" and states[8] == "~" and states[4] == "~" and states[6] == "~":
    answer = 5
elif states[3] == "~" and states[6] == "~" and states[9] == "~" :
    answer = 6
elif states[4] == "~" and states[5] == "*" and states[7] == "~" and states[8] == "~":
    answer = 7
elif states[7] == "~" and states[8] == "~" and states[9] == "~" :
    answer = 8
elif states[5] == "*" and states[6] == "~" and states[8] == "~" and states[9] == "~":
    answer = 9

print(answer)
