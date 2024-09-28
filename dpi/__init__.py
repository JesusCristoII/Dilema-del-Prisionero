from dilemma import Dilemma
from player import Player
from player import Cooperator
from player import Defector
from player import Tft
from player import Detective4MovsTft
from player import Grudger
from game import Game
from tournament import Tournament
from evolution import Evolution

dilemma = Dilemma(2, -1, 3, 0)

cooperator_player = Cooperator(dilemma, "cooperator")
defector_player = Defector(dilemma, "defector")
tft_player = Tft(dilemma, "tft")
grudger_player = Grudger(dilemma, "grudger")
detective_player = Detective4MovsTft(dilemma, "detective")

#Prueba 1
game = Game(tft_player, detective_player, n_rounds=10, error=0.2)
#game.play(do_print=True)

#prueba 2
all_players = (cooperator_player, defector_player, tft_player, grudger_player,
               detective_player)
tournament = Tournament(all_players, n_rounds=10, error=0.0, repetitions=1)
#tournament.play()
#tournament.plot_results()

#prueba 3
all_players = (defector_player, tft_player,detective_player)
evolution = Evolution(all_players, n_rounds=10, error=0.00, repetitions=1,
                      generations=10, reproductivity=0.2,
                      initial_population=(15, 5, 5))

evolution.play(True)