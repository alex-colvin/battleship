import unittest 
from ship import Ship

class TestShip(unittest.TestCase):
    def test_instance(self): 
        ship = Ship("Battleship", 4, "B")

        self.assertIsInstance(ship, Ship)
        self.assertEqual(ship.name, "Battleship")
        self.assertEqual(ship.size, 4)
        self.assertEqual(ship.x, 1)
        self.assertEqual(ship.y, 1)
        self.assertEqual(ship.identifyer, "B")
        self.assertEqual(ship.position, [1][1])
        self.assertEqual(ship.x_end, 5)
        self.assertEqual(ship.y_end, 5)
        







if __name__ == '__main__': 
    unittest.main()
