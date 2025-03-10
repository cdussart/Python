import sys
import random

dict_factories = dict()
dict_productions = dict()
dict_troops = dict()
dict_distances = dict()
nb_bombs_max = 2
nb_bombs = nb_bombs_max
init = True
bombed_factories = []

# Gather and store distance info
factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
for i in range(link_count):
  factory_1, factory_2, distance = input().split()
  if factory_1 not in dict_distances.keys():
    dict_distances[factory_1] = dict()
  if factory_2 not in dict_distances.keys():
    dict_distances[factory_2] = dict()
  dict_distances[factory_1][factory_2] = distance
  dict_distances[factory_2][factory_1] = distance

def get_factories_list(enemy = False):
  my_factories = []
  for factory_id in list(dict_factories.keys()):
    if factory_id in dict_factories and "owner" in dict_factories[factory_id] and dict_factories[factory_id]["owner"]  == "1" if not enemy else "-1":
      my_factories.append(factory_id)
  return my_factories

def get_enemy_factories_list():
  return get_factories_list(True)

def get_destinations_list(my_factories):
  destinations = list(dict_factories.keys())
  for factory_id in my_factories:
    destinations.remove(factory_id)
  return destinations

def get_best_factory_id(dict_productions, destination_ids):
  best_production = 0
  destination = -1
  for destination_id in destination_ids:
    if destination_id in dict_productions:
      if int(dict_productions[destination_id]) >= best_production :
        destination = destination_id 
        best_production = int(dict_productions[destination_id])
  return destination

def get_nearest_factory_id(dict_distances, my_factory_id, destinations):
  distance = 100
  destination = -1
  if len(dict_distances) > 0:
    if my_factory_id in dict_distances:
      distances = dict_distances[my_factory_id]
      if len(distances) > 0:
        for fact, dist in distances.items():
          if fact in destinations:
            if int(dist) < distance:
              distance = int(dist)
              destination = fact
  return destination

def get_strongest_factory_id(factories, destination_ids):
  nb_cyborgs = 0
  destination = -1
  for destination_id in destination_ids:
    if destination_id in factories and "nb_cyborgs" in factories[destination_id]:
      if int(factories[destination_id]["nb_cyborgs"]) >= nb_cyborgs :
        destination = destination_id 
        nb_cyborgs = int(factories[destination_id]["nb_cyborgs"])
  return destination

def get_production(dict_productions, factory_id):
  return int(dict_productions[factory_id]) if factory_id in dict_productions else -1

def get_distance(dict_distances, source_id, destination_id):
  if source_id in dict_distances and destination_id in dict_distances[source_id]:
    return int(dict_distances[source_id][destination_id])
  elif destination_id in dict_distances and source_id in dict_distances[destination_id]:
    return int(dict_distances[destination_id][source_id])
  else:
    return 0

def is_cyborg_targeted(dict_troops, destination_id):
  targeted = False
  for troop in dict_troops:
    if dict_troops[troop]["dest"] == destination_id and dict_troops[troop]["owner"] == "1":
      targeted = True 
      break
  return targeted

# game loop
while True:

  # Gather data for the round
  entity_count = int(input())  # the number of entities (e.g. factories and troops)
  for i in range(entity_count):
    inputs = input().split()
    entity_id = inputs[0]
    entity_type = inputs[1]
    owner = inputs[2]
    arg_2 = inputs[3]
    arg_3 = inputs[4]
    arg_4 = inputs[5]
    arg_5 = inputs[6]
    if entity_type == "FACTORY":
      if entity_id not in dict_factories:
        dict_factories[entity_id] = dict()
      dict_factories[entity_id]["owner"] = owner
      dict_factories[entity_id]["nb_cyborgs"] = arg_2      
      if init:
        dict_factories[entity_id]["production"] = arg_3
        dict_productions[entity_id] = arg_3
    elif(entity_type == "TROOP"):
      if entity_id not in dict_troops:
        dict_troops[entity_id] = dict()
      dict_troops[entity_id]["owner"] = owner
      dict_troops[entity_id]["source"] = arg_2
      dict_troops[entity_id]["dest"] = arg_3
      dict_troops[entity_id]["nb_cyborgs"] = arg_4
      dict_troops[entity_id]["distance_left"] = arg_5

  my_factories = get_factories_list()  
  destinations = get_destinations_list(my_factories)
  dict_distances_copy = dict_distances

  actions = "WAIT"

  # For each of my factories, decide what to do
  for factory in my_factories:

    # Count my cyborgs
    nb_cyborgs_factory = int(dict_factories[factory]["nb_cyborgs"]) if "nb_cyborgs" in dict_factories[factory] else 100

    # Destroy the factories with the highest number of cyborgs. But not at the very first turn, since they'll likely leave the factory to invade other factories.
    if not init:
      if nb_bombs > 0:
        enemy_destinations = get_enemy_factories_list()
        best_factory_id = get_strongest_factory_id(dict_factories, enemy_destinations)
        already_targeted = is_cyborg_targeted(dict_troops, best_factory_id)
        if best_factory_id != -1 and not already_targeted and best_factory_id not in bombed_factories and best_factory_id in dict_factories and "nb_cyborgs" in dict_factories[best_factory_id] and int(dict_factories[best_factory_id]["nb_cyborgs"]) > 20:
          actions += ";BOMB "+factory+" "+str(best_factory_id)
          bombed_factories.append(best_factory_id)
          nb_bombs -= 1
    else:
      init = False

    # Send n cyborgs to the nearest factory
    while nb_cyborgs_factory > 0:    
      nearest_factory_id = get_nearest_factory_id(dict_distances_copy, factory, destinations)      
      if nearest_factory_id != -1:
        if "nb_cyborgs" in dict_factories[nearest_factory_id]:
          nb_cyborgs_sent = int(dict_factories[nearest_factory_id]["nb_cyborgs"]) + get_production(dict_productions, nearest_factory_id) * get_distance(dict_distances, factory, nearest_factory_id)
          if nb_cyborgs_sent < nb_cyborgs_factory:
            del dict_distances_copy[factory][nearest_factory_id]
        else:
          nb_cyborgs_sent = 100
        actions += ";MOVE "+factory+" "+str(nearest_factory_id)+" "+str(nb_cyborgs_sent)        
        nb_cyborgs_factory -= nb_cyborgs_sent
      else:
        best_factory_id = get_best_factory_id(dict_productions, destinations)
        if best_factory_id != -1:
          nb_cyborgs_sent = int(dict_factories[best_factory_id]["nb_cyborgs"]) +1 if "nb_cyborgs" in dict_factories[best_factory_id] else 100
          actions += ";MOVE "+factory+" "+str(best_factory_id)+" "+str(nb_cyborgs_sent) 
          if nb_cyborgs_sent < nb_cyborgs_factory:
            destinations.remove(best_factory_id)
          nb_cyborgs_factory -= nb_cyborgs_sent
        else:
          nb_cyborgs_factory = 0

  print(actions)