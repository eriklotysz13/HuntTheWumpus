import random


class Cave:
    def __init__(self):
        self.rooms = self.generate_cave()
        self.wumpus = random.randint(0, 19)
        self.pits = random.sample([i for i in range(20) if i != self.wumpus], 2)
        self.bats = random.sample([i for i in range(20) if i not in self.pits and i != self.wumpus], 2)
        self.player = random.choice([i for i in range(20) if i not in self.pits and i != self.wumpus])
        self.arrow = 1
        self.alive = True
        self.won = False

    def generate_cave(self):
        # Each room has 3 unique connections
        cave = {}
        for i in range(20):
            connections = set()
            while len(connections) < 3:
                room = random.randint(0, 19)
                if room != i:
                    connections.add(room)
            cave[i] = list(connections)
        return cave

    def check_hazards(self):
        if self.player == self.wumpus:
            print("You were eaten by the Wumpus!")
            self.alive = False
        elif self.player in self.pits:
            print("You fell into a bottomless pit!")
            self.alive = False
        elif self.player in self.bats:
            print("Bats carried you to another room!")
            self.player = random.choice([i for i in range(20) if i != self.player])
            self.check_hazards()

    def move(self, room):
        if room not in self.rooms[self.player]:
            print("Invalid move. Try again.")
            return
        self.player = room
        self.check_hazards()
    
    def shoot(self, path):
        if self.arrow == 0:
            print("You have no arrows!")
            return
        self.arrow -= 1
        for room in path:
            if room == self.wumpus:
                print("You hear a scream! You killed the Wumpus!")
                self.won = True
                return
            if room not in self.rooms.get(self.player, []):
                print("Arrow hit a wall and broke.")
                return
        print("You missed!")
