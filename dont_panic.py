# Vous devez aider les clones à atteindre la sortie pour s'échapper de la zone du générateur.
# L'objectif est d'obtenir 100% avec le code le plus court possible.
# 
# Règles
# 
# La zone est rectangulaire et de taille variable. Elle est composée de plusieurs étages (0 = étage inférieur)
# et chaque étage comporte plusieurs positions possible pour les clones
# (0 = position la plus à gauche, width - 1 = position la plus à droite).
# 
# L'objectif est de sauver au moins un clone en un nombre limité de tours.
# 
# En détail :
# 
# Les clones sortent d'un unique générateur à intervalles réguliers, tous les 3 tours.
# Le générateur est placé à l'étage 0. Les clones sortent en se dirigeant vers la droite.# 
# Les clones avancent d'une position par tour en ligne droite, dans leur direction actuelle.# 
# Un clone est détruit par un laser s'il dépasse la position 0 ou la position width - 1.
# La zone dispose d'ascenseurs pour monter d'un étage à l'autre. Quand un clone arrive sur une position
# où se trouve un ascenseur, il monte d'un étage. Monter d'un étage prend un tour de jeu.
# Au tour suivant le clone continue sa progression dans la direction qu'il avait avant de monter.
# À chaque tour vous pouvez soit ne rien faire, soit bloquer le clone de tête
# (c-à-d celui qui est sorti le plus tôt).
# Une fois qu'un clone est bloqué, vous ne pouvez plus agir dessus. Le clone suivant prend le rôle
# de clone de tête et peut être bloqué à son tour.# 
# Quand un clone avance ou se trouve sur une position sur laquelle se situe un clone bloqué,
# il change de direction.# 
# Si un clone bloque au pied d'un ascenseur, l'ascenseur ne peut plus être utilisé.
# Quand un clone atteint l'étage et la position de l'aspirateur, il est sauvé et disparait de la zone.
# Note : Pour ce puzzle il n'y a au maximum qu'un ascenseur par étage

# Get general input data.
# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

# Get elevators data
# elevator_floor: floor on which this elevator is found
# elevator_pos: position of the elevator on its floor

elevators = dict()
for i in range(nb_elevators):
  elevator_floor, elevator_pos = [int(j) for j in input().split()]
  elevators[elevator_floor] = elevator_pos

# Game loop
while True:


    # Get leading clone data
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # clone_direction: direction of the leading clone: LEFT or RIGHT
    inputs = input().split()
    clone_floor = int(inputs[0])
    clone_pos = int(inputs[1])
    clone_direction = inputs[2]

    # Find the exit position
    exit_position = exit_pos if clone_floor == exit_floor else elevators[clone_floor] if clone_floor in elevators else clone_pos
    
    # If the clone is at the exit position (elevator), wait for it to go inside
    if(clone_pos == exit_position):
      print("WAIT")

    # Else, if the clone is not oriented correctly block it, otherwise let it go forward
    else:
      right_direction = "RIGHT" if clone_pos < exit_position else "LEFT"
      print("BLOCK" if clone_direction != right_direction else "WAIT")
