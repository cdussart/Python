# L'objectif de votre programme est de faire atterrir, sans crash, la capsule "Mars Lander"
# qui contient le rover Opportunity. La capsule “Mars Lander” permettant de débarquer le rover est pilotée par
# un programme qui échoue trop souvent dans le simulateur de la NASA.
# 
# Sous forme de jeu, le simulateur place Mars Lander dans une zone du ciel de Mars.
# La zone fait 7000m de large et 3000m de haut.
# Il existe une unique zone d'atterrissage plane sur la surface de Mars et elle mesure au moins 1000 mètres de large.
# 
# Toutes les secondes, en fonction des paramètres d’entrée (position, vitesse, fuel, etc.), le programme doit fournir
# le nouvel angle de rotation souhaité ainsi que la nouvelle puissance des fusées de Mars Lander: 
# Angle de -90° à 90°.
# Puissance des fusées de 0 à 4.
# 
# Le jeu modélise une chute libre sans atmosphère. La gravité sur Mars est de 3,711 m/s².
# Pour une puissance des fusées de X, on génère une poussée équivalente à X m/s² et on consomme X litres de fuel.
# Il faut donc une poussée de 4 quasi verticale pour compenser la gravité de Mars.
# Pour qu’un atterrissage soit réussi, la capsule doit :
#  - atterrir sur un sol plat
#  - atterrir dans une position verticale (angle = 0°)
#  - la vitesse verticale doit être limitée ( ≤ 40 m/s en valeur absolue)
#  - la vitesse horizontale doit être limitée ( ≤ 20 m/s en valeur absolue)
# 

G = 3.711
MAX_VS = 40
DEF_ANGLE = 30

"""
Determines whether your speed (both horizontal and vertical) is ok for landing.
It calculates the coordinates of your landing point assuming you start reducing your speed now,
and returns whether the horizontal point is farther than the target and the vertical point is above the target.
x : horizontal position
x_center : horizontal position of the target (in the center of the landing area)
h_speed : horizontal speed
y : vertical position
height_plateau : height of the landing area
v_speed : vertical speed
Returns an array of two booleans : if you stop now, will your x be < x_target and will your y be > y_target
"""
def can_stop_on_time(x, x_center, h_speed, y, height_plateau, v_speed):

  res = {"horizontal_distance" : False, "altitude" : False}

  if(y < height_plateau):
    return res

  # Horizontal speed
  h_distance = abs(x - x_center)
  h_distance_before_stop = 0
  current_h_speed = abs(h_speed)
  diminution_h_max = DEF_ANGLE / 90 * 4

  # Vertical altitude
  altitude = y - height_plateau
  current_v_speed = v_speed
  diminution_altitude = -(4 - G)
  
  while(current_h_speed > 0 and altitude > 0):
    h_distance_before_stop += current_h_speed
    current_h_speed -= diminution_h_max
    altitude += current_v_speed # speed < 0 means you're falling
    current_v_speed += diminution_altitude
  
  res["horizontal_distance"] = h_distance_before_stop < h_distance
  res["altitude"] = altitude > 100

  return res

"""
Provides your desired angle according to your position and what phase you are currently in.
X : horizontal position
x_center : horizontal position of the target (in the center of the landing area)
phase : ["acceleration" | "stopping" | "went_too_far", "inverse_stopping"]; basically, should you be facing the target or not
situation_initiale : ["left"|"right"]; meaning, if you started "left" of your target, you want to go to the right, and vice-versa.
"""
def get_max_angle(X, x_center, phase = "acceleration", initial_situation = "left"):
  if(phase == "acceleration"):
    if(X < x_center):
      return -DEF_ANGLE
    else:
      return DEF_ANGLE
  elif(phase == "stopping"):
    if(initial_situation == "left"):
      return DEF_ANGLE   
    else:
      return -DEF_ANGLE
  elif(phase == "went_too_far"):
    if(initial_situation == "left"):
      return DEF_ANGLE
    else:
      return -DEF_ANGLE
  elif(phase == "inverse_stopping"):
    if(initial_situation == "left"):
      return -DEF_ANGLE;   
    else:
      return DEF_ANGLE
  else:
    return 0

# Find the landing area using the first input lines (provide the coordinates of the points of the whole area)
x_min = -1
x_max = 15000
height_plateau = 0
prev_x = -1
prev_y = -1
coordinates = dict()
n = int(input())
for i in range(n):
    land_x, land_y = [int(j) for j in input().split()]
    coordinates[land_x] = land_y
    if(land_y != prev_y):
      prev_x = land_x
      prev_y = land_y
    else:
      if(land_x - prev_x >= 1000):
        x_min = prev_x
        x_max = land_x
        height_plateau = land_y

# Initialisation of variables
x_center = (x_max + x_min)/2
initial_situation = ""
initial_height = -1
acceleration = True
slowdown = False
comeback = False
landing = False

# Game loop
while (True):

  # HS: the horizontal speed (in m/s), can be negative.
  # VS: the vertical speed (in m/s), can be negative.
  # F: the quantity of remaining fuel in liters.
  # R: the rotation angle in degrees (-DEF_ANGLE to DEF_ANGLE).
  # P: the thrust power (0 to 4).
  x, y, hs, vs, f, r, p = [int(i) for i in input().split()]

  if(initial_situation == ""):
    initial_situation = "left" if x < x_min else "right"
  if(initial_height == -1):
    initial_height = y - height_plateau

  angle = 0
  thrust = 4

  # During the acceleration phase :
  if(acceleration):

    canstop_and_altitudeok = can_stop_on_time(x, x_center, hs, y, height_plateau, vs)
    
    # If altitude is high enough
    if(canstop_and_altitudeok["altitude"]):

      # If the target distance is far enough, you may accelerate
      if(canstop_and_altitudeok["horizontal_distance"]):
        angle = get_max_angle(x, x_center, "acceleration")
        
      # Otherwise, you must start stopping now
      else:
        angle = get_max_angle(x, x_center, "stopping", initial_situation)
        acceleration = False
        slowdown = True
    
  # During the stopping / slowing down phase :
  elif(slowdown):
        
    went_too_far = initial_situation == "left" and x > x_max or initial_situation == "right" and x < x_min
    
    # If you're above the landing area :
    if(not went_too_far):

      # If your horizontal speed is still a bit high, the angle must be used to keep slowing down
      if(abs(hs) > 2):
        angle = get_max_angle(x, x_center, "stopping", initial_situation)
        
      # Otherwise, you go for a 0 angle and land
      else:
        angle = 0
        slowdown = False
        landing = True
        
    # If you're not above the landing area though the acceleration phase is over, it means you've gone too far.
    else:
      angle = get_max_angle(x, x_center, "went_too_far", initial_situation)
      slowdown = False
      comeback = True
    
  # If you've gone too far and are coming back to the landing area :
  elif(comeback):
      
    above = x > x_min and x < x_max

    # If you're not above, keep going
    if(not above):
      angle = get_max_angle(x, x_center, "went_too_far", initial_situation)
        
    # If you're above, you may land
    else:
      comeback = False
      landing = True
    
  # Landing phase
  else:

    # If your horizontal speed is still a bit high, the angle must be used to keep slowing down
    if(abs(hs) > 2):
      angle = get_max_angle(x, x_center, "inverse_stopping", initial_situation)
      
    # Otherwise, you go for a 0 angle and land
    else:
      angle = 0
      if(abs(vs) < MAX_VS):
        thrust = 3

  # Play your chosen angle and thrust
  print(str(angle)+" "+str(thrust))