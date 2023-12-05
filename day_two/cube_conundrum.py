import os, re

def validate_game_entry(color, number):
    valid_contents = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    if color in valid_contents.keys():
        if number <= valid_contents[color]:
            return True

    return False

def cube_conundrum():
    valid_games_sum = 0
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
      valid_game = True
      for game in game_content:
        entries = game.split(',')
        for entry in entries:
          # iterate the entires to split into color and number
          number, color = entry.split()
          number = int(number)
          # validate the game entry
          if not validate_game_entry(color, number):
            valid_game = False
            break

      if valid_game:
        valid_games_sum += game_id

    return valid_games_sum

if __name__ == "__main__":
  print(cube_conundrum())
