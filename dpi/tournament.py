from player import Player
import itertools
from game import Game
#import matplotlib
#import matplotlib.pyplot as ply

class Tournament:

    # Este método ya está implementado
    def __init__(self, players: tuple[Player, ...],
                       n_rounds: int = 100,
                       error: float = 0.0,
                       repetitions: int = 2):
        """
        All-against-all tournament

        Parameters:
            - players (tuple[Player, ...]): tuple of players that will play the
         tournament
            - n_rounds (int = 100): number of rounds in the game
            - error (float = 0.0): error probability (in base 1)
            - repetitions (int = 2): number of games each player plays against
         the rest
        """

        self.players = players
        self.n_rounds = n_rounds
        self.error = error
        self.repetitions = repetitions

        # This is a key variable of the class. It is intended to store the
        # ongoing ranking of the tournament. It is a dictionary whose keys are
        # the players in the tournament, and its corresponding values are the
        # points obtained in their interactions with each other. In the end, to
        # see the winner, it will be enough to sort this dictionary by the
        # values.
        self.ranking = {player: 0.0 for player in self.players}  # initial vals


    def sort_ranking(self) -> None:
        """Sort the ranking by the value (score)"""
        sorted(self.ranking.keys(),key=lambda x: self.ranking[x])


    #pista: utiliza 'itertools.combinations' para hacer los cruces
    def play(self) -> None:
        """
        Main call of the class. It must simulate the championship and update
        the variable 'self.ranking' with the accumulated points obtained by
        each player in their interactions.
        """
        cruces = list(itertools.combinations(self.players,2))
        for i in range(len(cruces)*self.repetitions):
            player1 = cruces[i%len(cruces)][0]
            player2 = cruces[i%len(cruces)][1]
            game = Game(player1,player2)
            game.play()
            player1.clean_history()
            player2.clean_history()
            self.ranking[player1] += game.score[0]
            self.ranking[player2] += game.score[1]


    def plot_results(self):
        """
        Plots a bar chart of the final ranking. On the x-axis should appear
        the names of the sorted ranking of players participating in the
        tournament. On the y-axis the points obtained.
        """
        print(self.ranking)
        #matplotlib.rcParams.update({'font.size' : 15})
        #plt.figure(figsize=(12,5))
        #plt.plot(self.ranking.keys(),self.ranking.values())
        #plt.xlabel('Jugadores')
        #plt.ylabel('Puntos')
        #plt.title('Resultados del Torneo')
        #plt.show