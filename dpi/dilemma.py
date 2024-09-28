from abc import abstractmethod
import numpy as np
import numpy.typing as npt
import itertools 

class Dilemma:

    def __init__(self, cc: float, cd: float, dc: float, dd: float):
        """
        Represents a 2x2 symmetric dilemma.

        Parameters:
            - cc (float): payoff for mutual cooperation
            - cd (float): payoff when one cooperates, but the opponent defects
            - dc (float): payoff when one defects, and the opponent cooperates
            - dd (float): payoff for mutual defection
        """
        self.__recompensas = np.array([(cc,cd),(dc,dd)], dtype= float)


    @property
    @abstractmethod
    def payoff_matrix(self) -> npt.NDArray[np.floating]:
        """
        Symmetric pay-off matrix of the dilema

        Returns:
            - 2x2 np array of the matrix
        """
        return self.__recompensas


    @abstractmethod
    def evaluate_result(self, a_1: int, a_2: int) -> tuple[float, float]:
        """
        Given two actions, returns the payoffs of the two players.

        Parameters:
            - a_1 (int): action of player 1 ('C' or 'D', i.e. '1' or '0')
            - a_2 (int): action of player 2 ('C' or 'D', i.e. '1' or '0')

        Returns:
            - tuple of two floats, being the first and second values the payoff
            for the first and second player, respectively.
        """
        return self.payoff_matrix[a_1][a_2],self.payoff_matrix[a_2][a_1]
    
