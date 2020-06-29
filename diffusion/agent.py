from mesa import Agent


class Environment(Agent):
    """
    A cell representing the Environment that will hold the chemical being
    disbursed, and then reduce that amount through diffusion and evaporation.
    """

    def __init__(self, pos, model):
        """
        Create a new cell.
        Args:
            pos: The cell's coordinates on the grid.
            model: standard model reference for agent.
        """
        super().__init__(pos, model)
        self.pos = pos
        self.amount = 0.0

    def step(self):
        """
        Find the sum of chemical in the neighboring environment, including this
        cell, then set this cell to be the diffused and evaporated amount.
        """
        all_p = self.amount
        neighbors = self.model.grid.get_neighbors(self.pos, True)
        for n in neighbors:
            all_p += n.amount
        ave_p = all_p / (len(neighbors) + 1)

        self._nextAmount = (1 - self.model.evaporate) * \
            (self.amount + (self.model.diffusion * \
                                (ave_p - self.amount)))

        if self._nextAmount < self.model.lowerbound:
            self._nextAmount = 0

    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.amount = self._nextAmount

    def add(self, amount):
        """
        Add the amount to the cell's amount
        """
        self.amount += amount

    def get_pos(self):
        return self.pos
