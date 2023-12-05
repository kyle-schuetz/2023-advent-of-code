import re

def find_min_cube_set_sum():

    sum = 0
    # read the input file into memory
    with open("input_file.txt", "r") as f:
            lines = f.readlines()

    # iterate each of the lines (game entries)
    for line in lines:
      line = line.rstrip('\n')
      # split the line into game id,  game content
      game_id, game_content = line.split(':')
      # get only digit from game id
      game_id = int(re.findall(r'\d+', game_id)[0])
      # split game content into individual games
      game_content = game_content.split(';')
      # iterate each game entry to ensure validity of provided game entries
      green = 0
      red = 0
      blue = 0
      for game in game_content:
        entries = game.split(',')
        for entry in entries:
          # iterate the entires to split into color and number
          number, color = entry.split()
          number = int(number)
          # validate the game entry
          if color == 'blue':
              blue = max(blue, number)
          elif color == 'green':
              green = max(green, number)
          else:
              red = max(red, number)
      power = green * blue * red
      sum += power

    return sum


if __name__ == "__main__":
  print(find_min_cube_set_sum())
