def get_distance(x1, y1, x2, y2):
  """
  Returns the distance between two points, being given the (x,y) coordinates of these two points.
  x1 : x of the first point
  y1 : y of the first point
  x2 : x of the second point
  y2 : y of the second point
  """
  return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

while True:

  x, y = [int(i) for i in input().split()] # my coordinates
  human_count = int(input()) # number of remaining humans

  # Locate all humans
  for i in range(human_count):
    human_id, human_x, human_y = [int(j) for j in input().split()]

  # Locate all zombies
  zombie_count = int(input())
  nearest_coordinates = []
  nearest_distance = 30000
  for i in range(zombie_count):
    zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]

    distance_i = get_distance(zombie_xnext, zombie_ynext, x, y)
    if( distance_i < nearest_distance):
      nearest_distance = distance_i
      nearest_coordinates = [zombie_xnext, zombie_ynext]

  # Go to nearest zombie
  print(str(nearest_coordinates[0])+" "+str(nearest_coordinates[1]))
