from player import Player

class Game:

    # Este método ya está implementado
    def __init__(self, player_1: Player,
                       player_2: Player,
                       n_rounds: int = 100,
                       error: float = 0.0):
        """
        Game class to represent an iterative dilema

        Parameters:
            - player_1 (Player): first player of the game
            - player_2 (Player): second player of the game
            - n_rounds (int = 100): number of rounds in the game
            - error (float = 0.0): error probability (in base 1)
        """

        assert n_rounds > 0, "'n_rounds' should be greater than 0"

        self.player_1 = player_1
        self.player_2 = player_2
        self.n_rounds = n_rounds
        self.error = error

        self.score = (0.0, 0.0)  # this variable will store the final result of
                                 # the game, once the 'play()' function has
                                 # been called. The two values of the tuple
                                 # correspond to the points scored by the first
                                 # and second player, respectively.


    def play(self, do_print: bool = False) -> None:
        """
        Main call of the class. Play the game.
        Stores the final result in 'self.score'

        Parameters
            - do_print (bool = False): if True, should print the ongoing
            results at the end of each round (i.e. print round number, last
            actions of both players and ongoing score).
        """
        for i in range(self.n_rounds):
            self.player_1.history.append(self.player_1.strategy(self.player_2))
            self.player_2.history.append(self.player_2.strategy(self.player_1))
            self.score = self.player_1.compute_scores(self.player_2)
            if do_print:
                print(self.score)


    def play2(self, do_print: bool = False) -> None:
        """
        Main call of the class. Play the game.
        Stores the final result in 'self.score'

        Parameters
            - do_print (bool = False): if True, should print the ongoing
            results at the end of each round (i.e. print round number, last
            actions of both players and ongoing score).
        """
        for i in range(self.n_rounds):
            if random.random() < self.error:
                'C' = 'D'
                'D' = 'C'

                self.player_1.history.append(self.player_1.strategy(self.player_2))
                self.player_2.history.append(self.player_2.strategy(self.player_1))
                self.score = self.player_1.compute_scores(self.player_2)

            else:
                self.player_1.history.append(self.player_1.strategy(self.player_2))
                self.player_2.history.append(self.player_2.strategy(self.player_1))
                self.score = self.player_1.compute_scores(self.player_2)

            if do_print:
                print(self.score)


