from player import Player

player1 = Player('Player1')
player2 = Player('Player2')

# initial setup
player1.gameboard.generate_grid(10,20)
player1.place_ships()
player2.gameboard.generate_grid(10,20)
player2.place_ships()

#battle sequence
player1.fire(player2.ships)