import random

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder
    Attributes:
        _piles (list): The number of piles of stones.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """

        self._piles = []
        self._prepare()
        


    def to_string(self):
        """Converts the board data to its string representation.
        Args:
           self (Board): an instance of Board.
        Returns:
            string: A representation of the current board.
        """ 
        
          
        board = ""

        border = "\n---------------------"

        board = board + border

        for (i, row) in enumerate(self._piles):
            line = ""
            while row != 0:
                     
                line = line + "O "
                    
                row -= 1
                    
            board = board + (f"\n{i}: {line}" )

        board += border  

        return board

        """
        * possible solution 
        
        text =  "\n--------------------"
        for pile, stones in enumerate(self._piles):
            text += (f"\n{pile}: " + "O " * stones)
        text += "\n--------------------"
        return text"""

    def apply(self, move):
        """Applies the given move to the playing surface. In this case, that 
        means removing a number of stones from a pile.
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """
        pile = move.get_pile()
        stones = move.get_stones()
        
        row = self._piles[pile]
        stones_left = row - stones
        
        if stones_left < 0:
            stones_left = 0

        self._piles[pile] = stones_left

        

        return self._piles
        
        """
        * possible solution will not let the value go below 0
            which breaks the code

        pile = move.get_pile()
        stones = move.get_stones()
        self._piles[pile] = max(0, self._piles[pile] - stones)"""

    def is_empty(self):
        """Determines if all the stones have been removed from the board.
        
        Args:
            self (Board): an instance of Board.
        Returns:
            boolean: True if the board has no stones on it; false if otherwise.
        """
        
        empty = all(value == 0 for value in self._piles)
        if empty:
            return True
        else:
            return False

        """
        * possible solution

        empty = [0] * len(self._piles)
        return self._piles == empty"""   


    def _prepare(self):
        """Sets up the board with a random number of piles containing a random 
        number of stones.
        
        Args:
            self (Board): an instance of Board.
        """
        
        num_piles = random.randint(2, 5)

        for i in range(num_piles):
                num_stones = random.randint(1, 9)
                self._piles.append(num_stones)
        
        return self._piles
        
        

