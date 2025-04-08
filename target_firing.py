import math

# Your spaceship is under attack by aliens!
# (It's actually your friend's spaceship, so the situation is even worse).
# Luckily your spaceship is equipped with an antimatter beam, while the aliens only have cheap
# (but still dangerous) laser pointers. Can you destroy all alien spaceships safely, or should you flee?
# 
# As the AI within the ship's computer, your goal is to determine the optimal order of alien spaceships to destroy
# such that you leave the encounter with the maximum strength of your shields.
# Print the remaining strength of the shields, or FLEE if your spaceship is predicted to take more damage
# than your shields can handle. Your friend will not forgive you if the ship is damaged.
# 
# The encounter can be modeled by turn-based combat. Your spaceship's shields begin with 5000 strength.
# You are fighting against N alien spaceships of various properties. These properties are:
# SHIP - the type of the spaceship, which can be either FIGHTER or CRUISER,
# HP - the amount of damage the spaceship can receive before being destroyed,
# ARMOR - the damage reduction of the spaceship, and
# DAMAGE - the amount of damage the spaceship deals per turn.
# 
# On each turn, all alien spaceships reduce your ship's shields by DAMAGE as your antimatter beam charges,
# and then one spaceship takes damage from your antimatter beam.
# Your beam deals 10 base damage to a spaceship.
# The actual damage that the spaceship receives is decreased by the spaceship's ARMOR.
# Luckily, your antimatter beam does double damage to FIGHTER-class spaceships
# hence, the damage that FIGHTER-class spaceships receives is 20 - ARMOR.
# Your antimatter beam always deals at least 1 damage, even if the target spaceship's ARMOR is greater than
# your beam's damage.
# 
# Input
# Line 1: An integer N for the number of alien spaceships.
# Next N lines: One string followed by three integers, space-separated, representing
# the SHIP type, HP, ARMOR, and DAMAGE of the alien spaceship.
# 
# Output
# An integer representing the maximum strength of shields left after an optimal encounter,
# or FLEE if your spaceship will take hull damage (shield strength < 0).

DAMAGE_PER_TURN = 10
TYPE_CRUISER = "CRUISER"

# Calculates the damages received on one turn, based on the damage each ship of the fleet can inflict.
# @param ships : the ships of the fleet
# @return : the sum of the damages received
def get_sum_damages(ships):
  sum_damages = 0
  for ship_id, ship in ships.items():
    sum_damages += ship["damage_given"]
  return sum_damages

# Sorts the ratios of the ships and returns the index of the best ship.
# The ratios are calculated directly at initialisation and are based on damages inflicted / received, ship armour, ship type
# @param ships : the ships of the fleet
# @return : the index of the best ship ie the next target
def get_best_ratio(ships):
  ratio = -1
  i = 0
  for ship_id, ship in ships.items():
    current_ratio = ship["ratio"]
    if(current_ratio > ratio):
      ratio = current_ratio
      i = ship["i"]
  return {"best_i" : i, "best_ratio" : ratio}

# Retrieve the data for each alien spaceship
ships = dict()

n = int(input())
for i in range(n):
  inputs = input().split()
  ship = inputs[0]
  hp = int(inputs[1])
  armor = int(inputs[2])
  damage = int(inputs[3])
  damage_per_turn = DAMAGE_PER_TURN if ship == TYPE_CRUISER else DAMAGE_PER_TURN * 2
  max_damage_per_turn = 1 if armor >= damage_per_turn else damage_per_turn - armor
  turns_to_die = math.ceil(hp / max_damage_per_turn)
  ships[i] = {
    "i" : i,
    "max_damage_received" : hp,
    "max_damage_per_turn" : max_damage_per_turn,
    "damage_given" : damage,
    "turns_to_die" : turns_to_die,
    "ratio" : damage / turns_to_die
  }

shield = 5000
damages_per_turn = get_sum_damages(ships)

# Choose a target
target_info = get_best_ratio(ships)
target = ships[target_info["best_i"]]
target_damage_per_turn = target["max_damage_per_turn"]

# Game loop
while(shield > 0 and len(ships)):

  # Receive damages for the number of turns I'm targeting the chosen target
  shield -= (damages_per_turn * target["turns_to_die"])

  # Fire on the chosen target / Decrease the chosen target strength for the number of turns I'm targeting the chosen target
  target["max_damage_received"] -= target_damage_per_turn * target["turns_to_die"]

  # If the target is destroyed (should be!), choose another one
  if(target["max_damage_received"] <= 0):
    del ships[target["i"]]
    if(len(ships)):
        damages_per_turn = get_sum_damages(ships)
        target_info = get_best_ratio(ships)
        target = ships[target_info["best_i"]]
        target_damage_per_turn = target["max_damage_per_turn"]

# Echo my strength at the end of the game, or flee if no strength left
print(shield if shield >= 0 else "FLEE")