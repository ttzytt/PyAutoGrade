'''
     /   \
    /     \
   /       \
  /         \
 /           \
/             \
'''

class Road():
    def __init__(self, width, obstacles = [], index = 0):
        self.width = width
        self.obstacles = obstacles
        self.index = index

    def get_ascii_road(self, length):
        road_rows = []
        max_width = self.width + 2 * length
        for i in range(length): 
            
            
            obstacle_margin = ((self.width + 2 * i) - 1) / (self.width-1)) - 1
            road_middle = (" "*obstacle_margin).join(self.obstacles[self.index + i])
            
            road_part = f"/{int(self.width + 2 * i) * ' '}\\"
            margin = int((max_width - (self.width + 2 * i + 2)) / 2) * ' '
            road_rows.append(margin + road_part + margin)
        return '\n'.join(road_rows)

road = Road(3)
print(road.get_ascii_road(30))
