import sys
import math
import random

# Votre virus a créé une backdoor sur le réseau Bobnet vous permettant d'envoyer
# de nouvelles instructions au virus en temps réél.
# Vous décidez de passer à l'attaque active en empêchant Bobnet de communiquer sur son propre réseau interne.
# Le réseau Bobnet est divisé en sous-réseaux.
# Sur chaque sous-réseau un agent Bobnet a pour tâche de transmettre de l'information
# en se déplaçant de noeud en noeud le long de liens et d'atteindre une des passerelles
# qui mène vers un autre sous-réseau.
# Votre mission est de reprogrammer le virus pour qu'il coupe les liens dans le but d'empêcher
# l'agent Bobnet de sortir de son sous-réseau et ainsi d'informer le hub central de la présence de notre virus.

links = dict()
exits = list()
# n_nodes: the total number of nodes in the level, including the gateways
# n_links: the number of links
# n_exits: the number of exit gateways
n_nodes, n_links, n_exits = [int(i) for i in input().split()]

# Gather links data
for i in range(n_links):
  # n1: N1 and N2 defines a link between these nodes
  n1, n2 = [str(j) for j in input().split()]
  if n1 not in links:
    links[n1] = []
  if n2 not in links[n1]:
    links[n1].append(n2)
  if n2 not in links:
    links[n2] = []
  if n1 not in links[n2]:
    links[n2].append(n1)

for i in range(n_exits):
  ei = input() # the index of a gateway node
  exits.append(ei)

# game loop
while True:
  cut = "-1"
  bobNodeId = input()  # The index of the node on which the Bobnet agent is positioned this turn

  # If Bobnet is about to reach the exit, cut the access
  for exit in exits:
    if exit in links[bobNodeId]:
      cut = exit
  if cut != "-1":
    links[cut].remove(bobNodeId)
    links[bobNodeId].remove(cut)
  # Otherwise, take any exit and cut one of its links 
  else:
    if len(exits) > 0:
      cut = random.choice(exits)
      bobNodeId = random.choice(links[cut])
    else:
      cut = random.choice(links[bobNodeId])

  print(bobNodeId+" "+cut)
