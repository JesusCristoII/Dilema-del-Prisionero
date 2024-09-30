from dilemma import Dilemma
from abc import ABC,abstractmethod

C = 0
D = 1

class Player(ABC):

    # Este método ya está implementado
    @abstractmethod
    def __init__(self, dilemma: Dilemma, name: str = ""):
        """
        Abstract class that represents a generic player

        Parameters:
            - name (str): the name of the strategy
            - dilemma (Dilemma): the dilemma that this player will play
        """

        self.name = name
        self.dilemma = dilemma

        self.history  = []  # This is the main variable of this class. It is
                            # intended to store all the history of actions
                            # performed by this player.
                            # Example: [C, C, D, D, D] <- So far, the
                            # interaction lasts five rounds. In the first one,
                            # this player cooperated. In the second, he also
                            # cooperated. In the third, he defected. Etc.


    # Este método ya está implementado
    @abstractmethod
    def strategy(self, opponent) -> int:
        """
        Main call of the class. Gives the action for the following round of the
        interaction, based on the history

        Parameters:
            - opponent (Player): is another instance of Player.

        Results:
            - An integer representing Cooperation (C=0) or Defection (D=1)
        """
        pass


    def compute_scores(self, opponent) -> tuple[float, float]:
        """
        Compute the scores for a given opponent

        Parameters:
            - opponent (Player): is another instance of Player.

        Results:
            - A tuple of two floats, where the first value is the current
            player's payoff, and the second value is the opponent's payoff.
        """
        resul1 = 0
        resul2 = 0
        for a_1,a_2 in zip(self.history,opponent.history):
            resul1 += self.dilemma.payoff_matrix[a_1][a_2]
            resul2 += self.dilemma.payoff_matrix[a_2][a_1]
        return (resul1,resul2)

    # Este método ya está implementado
    def clean_history(self):
        """Resets the history of the current player"""
        self.history = []


# A continuación se representan las 5 estrategias básicas del juego de Nicky Case

class Cooperator(Player):

    def __init__(self, dilemma: Dilemma, name: str = ""):
        self.dilemma = dilemma
        self.history = []
        """Cooperator"""


    def strategy(self, opponent: Player) -> int:
        resul = C
        return resul
        """Cooperates always"""


class Defector(Player):

    def __init__(self, dilemma: Dilemma, name: str = ""):
        self.dilemma = dilemma
        self.history = []

        """Defector"""


    def strategy(self, opponent: Player) -> int:
        resul = D
        return resul
        """Defects always"""


class Tft(Player):

    def __init__(self, dilemma: Dilemma, name: str = ""):
        self.dilemma = dilemma
        self.history = []

        """Tit-for-tat"""


    def strategy(self, opponent: Player) -> int:

        if self.history == []:
            resul = C
        else:
            resul = opponent.history[-1]
        return resul
        
        
        """Cooperates first, then repeat last action of the opponent"""


class Grudger(Player):

    def __init__(self, dilemma: Dilemma, name: str = ""):
        self.dilemma = dilemma
        self.history = []


    def strategy(self, opponent: Player) -> int:
        if D in opponent.history:
            resul = D
        else:
            resul = C
        return resul
        

        """
        Cooperates always, but if opponent ever defects, it will defect for the
        rest of the game
        """


class Detective4MovsTft(Player):

    def __init__(self, dilemma: Dilemma, name: str = ""):
        self.dilemma = dilemma
        self.history = []
        """Four movement - tit for tat detective"""


    def strategy(self, opponent: Player) -> int:
        estado = None
        if len(self.history) == 0 or len(self.history) == 2 or len(self.history) == 3:
            estado = C
        elif len(self.history) == 1:
            estado = D
        
        else:
            if D in opponent.history[4:0:-1] == D:
                estado = opponent.history[-1]
                    
            else:
                estado = D
        return estado


class Movimiento_Pendular(Player):
    def __init__(self, dilemma: Dilemma, name: str = ""):
        self.dilemma = dilemma
        self.history = []

    def perdon(self):   #funcion que nos ayuda a ver si el rival merece o no ser perdonado
        perdonar = False
        if random.random() < 0.3:
            perdonar = True
        return perdonar

    def strategy(self, opponent: Player) -> int:  #integramos dos compartamientos dentro de un mismo estilo de juego
        resul = None
        contador_castigos = 0 #contador para la estrategia a partir de la ronda 80

        if self.history == []:
            resul = C

        elif len(self.history) < 80:    # Antes de la ronda 80 aplicamos un tfd
             resul = opponent.history[-1]

        elif len(self.history) < 80 and opponent.history[-1] == D:
            if self.perdon():
                resul = C
            else:
                resul = D

        if len(self.history) > 80:
            if opponent.history[-1] == D:
                contador_castigos += 3

            if contador_castigos > 0:
                contador_castigos -= 1
                resul = D
            else:
                resul = C
                
        return resul



class Movimiento_Pendular2(Player):
    def __init__(self, dilemma: Dilemma, name: str = ""):
        self.dilemma = dilemma
        self.history = []
        self.contador_castigos = 0   #contador para la estrategia a partir de la ronda 80

    def perdon(self):   #funcion que nos ayuda a ver si el rival merece o no ser perdonado
        return random.random() < 0.3

    def analisis(self, opponent: Player):

        historial  = opponent.history
        cooperaciones = historial.count('C')
        cooperacion = (cooperaciones/80)

        return cooperacion

    def strategy(self, opponent: Player) -> int:  #integramos dos compartamientos dentro de un mismo estilo de juego
        
        resul = None

        if self.history == []:
            resul = C

        elif len(self.history) < 80:    # Antes de la ronda 80 aplicamos un tfd
            if opponent.history[-1] == D and not self.perdon():
                resul = D
            else:
                resul = C

        else:  #Analizamos el comportamiento que ha tenido el rival durante las rondas anteriores, 
                #En el caso de que haya cooperado la mayoría de las veces, no hay razón para castigar 
            if self.analisis(opponent) < 0.82: #Si el rival a cooperado menos de un 82% de las veces se le castigará

                if opponent.history[-1] == D:
                    self.contador_castigos = 2

                if self.contador_castigos > 0:
                    resul = D
                    self.contador_castigos -= 1
                else:
                    resul = C
            else:
                resul = opponent.history[-1]

        return resul
