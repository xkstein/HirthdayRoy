_world = {}
starting_position = (0, 0)

def load_rooms():
    with open('resources/map.txt, 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(x_max):
        cols = rows[y].split('\t')
        for x in range(x_max):
            room_name = cols[x].replace('\n', '')
            if room_name == 'StartingRoom':
                global starting_position
              starting_position = (x, y)
            _world[(x, y)] = None if room_name == '' else getattr(__import__('rooms'), room_name)(x, y)
            
