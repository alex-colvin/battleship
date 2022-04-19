from player import Player
from item import Item

player1 = Player('Player1')
player2 = Player('Player2')

# initial setup
player1.gameboard.generate_grid(10,20)
player1.place_ships()
player2.gameboard.generate_grid(10,20)
player2.place_ships()

#battle sequence
def fire_sequence (sender, recipient):
    sender.fire(recipient.ships)
    recipient.gameboard.set(sender.gameboard.curser, recipient.ships, True)

fire_sequence(player1, player2) 
fire_sequence(player1, player2)
