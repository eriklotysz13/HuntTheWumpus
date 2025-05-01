import random

class Cave:
    def generate_cave(self):
        # Each room has 3 unique connections, creating a basic map
        cave = {}
        for i in range(20):
            connections = set()
            while len(connections) < 3:
                room = random.randint(0, 19)
                if room != i:
                    connections.add(room)
            cave[i] = list(connections)
        return cave