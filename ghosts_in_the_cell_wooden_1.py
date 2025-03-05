import sys
import random

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
troops = dict()
factories = dict()
for i in range(link_count):
  factory_1, factory_2, distance = input().split()
  if factory_1 not in factories.keys():
    factories[factory_1] = dict()
  factories[factory_1][factory_2] = distance

# game loop
while True:
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
      if entity_id not in factories:
        factories[entity_id] = dict()
      factories[entity_id]["owner"] = owner
      factories[entity_id]["nb_cyborgs"] = arg_2
      factories[entity_id]["production"] = arg_3
    elif(entity_type == "TROOP"):
      if entity_id not in troops:
        troops[entity_id] = dict()
      troops[entity_id]["owner"] = owner
      troops[entity_id]["source"] = arg_2
      troops[entity_id]["dest"] = arg_3
      troops[entity_id]["nb_cyborgs"] = arg_4
      troops[entity_id]["distance_left"] = arg_5

  my_factories = []
  for factory_id in list(factories.keys()):
    if "owner" in factories[factory_id] and factories[factory_id]["owner"]  == "1":
      my_factories.append(factory_id)
  if len(my_factories) == 0:
    print("WAIT")
  else:
    source = random.choice(my_factories)

  destinations = list(factories.keys())
  for factory_id in my_factories:
    destinations.remove(factory_id)
  if len(destinations) == 0:
    print("WAIT")
  else:
    destination = random.choice(destinations)

  print("MOVE "+source+" "+destination+" 100")