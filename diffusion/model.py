from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import SingleGrid

from .agent import Environment

# derived from ConwaysGameOfLife
class Diffusion(Model):
    """
    Represents the diffusion of chemicals.
    """

    def __init__(self, height=50, width=50, evaporate=0.07, diffusion=0.3, initdrop=500, lowerbound=0.01):
        """
        Create a new playing area of (height, width) cells.
        """
        
        super().__init__()

        self.evaporate = evaporate
        self.diffusion = diffusion
        self.initdrop = initdrop
        self.lowerbound = lowerbound

        # Set up the grid and schedule.

        # Use SimultaneousActivation which simulates all the cells
        # computing their next state simultaneously.  This needs to
        # be done because each cell's next state depends on the current
        # state of all its neighbors -- before they've changed.
        self.schedule = SimultaneousActivation(self)

        # Use a simple grid, where edges wrap around.
        self.grid = SingleGrid(height, width, torus=True)

        # Place a cell at each location, with some initialized to
        # have chemical.
        for contents, (x, y) in self.grid.coord_iter():
            cell = Environment((x, y), self)
            if self.random.random() < 0.01:
                cell.add(self.initdrop)
            self.grid.place_agent(cell, (x, y))
            self.schedule.add(cell)

        self.running = True

    def step(self):
        """
        Have the scheduler advance each cell by one step
        """
        self.schedule.step()
