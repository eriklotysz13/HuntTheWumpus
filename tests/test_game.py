import unittest
from main import Cave

class TestWumpusGame(unittest.TestCase):
    def test_cave_has_20_rooms(self):
        cave = Cave()
        self.assertEqual(len(cave.rooms), 20)

    def test_move_to_valid_room(self):
        cave = Cave()
        current = cave.player
        next_room = cave.rooms[current][0]
        cave.move(next_room)
        self.assertEqual(cave.player, next_room)

if __name__ == "__main__":
    unittest.main()
