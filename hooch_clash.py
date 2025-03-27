# Wizarding is a full-time job when you're an elf. Collecting ingredients, refining spells, mixing potions, uncursing travellers…
# At the end of a busy day's work, elven wizards like to gather together at the magic tavern and play hooch clash.
# A clash works as follows:
# • the current king of the hill picks two glowing orbs and places them side by side on the table
# • the challenger picks two sparkling orbs and places them opposite
# • the bartender empties the hooch from each contender's orbs into a cauldron
# 
# If the glowing and sparkling liquids are provided in the exact same volume,
# the clash is valid and the winner is determined by fair coin toss.
# A valid clash is deemed fun if the four orbs on the table have a different size.
# A fun clash is as interesting as the challenger's two orbs are heterogeneous (different-sized),
# as measured by their outside, sparkling, surface area.
# 
# This tavern only has orbs of integral diameter from orbSizeMin to orbSizeMax. As many of each as you want, it's magic!
# 
# Can you help the challenger make a valid clash? Can you make it fun and interesting too?
# 
# Examples
# A clash opposing {9,10} to {1,12} is fun: all orbs are different-sized.
# A clash opposing {5,7} to {5,7} is valid: the contenders brought up equal volumes of glowing and sparkling hooch.
# A clash opposing {1,2} to {2,2} is possible: at least three size-2 orbs are available.
# 
# Assuming you could use them for a fun clash, challenging using {31,37} would be more interesting than using {25,32}.

# Read the orbs sizes
orb_size_min, orb_size_max = [int(i) for i in input().split()]
glowing_size_1, glowing_size_2 = [int(i) for i in input().split()]

# Calculate the total volume of the orbs of player 1
volume = (glowing_size_1 / 2)**3 + (glowing_size_2 / 2)**3

# Try and find 2 orbs that would reach the exact same volume, but with different orbs sizes
found = False
for i in range(orb_size_min, orb_size_max + 1):
  if not found:
    volumeI = (i / 2)**3
    for j in range(i, orb_size_max + 1):
        volume2 = volumeI + (j / 2)**3
        if volume2 == volume and i != glowing_size_1:
            print(str(i)+" "+str(j))
            found = True
            break

# If it's not possible with orbs of different volumes, then the only possibility is with same volumes, i.e. a valid clash.
if not found:  
  print("VALID")  