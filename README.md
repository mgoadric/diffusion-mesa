# Diffusion Model

## Summary

This is an agent-based simulation chemical diffusion in the environment.

Cells representing the Environment can hold the chemical being
disbursed. Each timestep this chemical is reduced in each cell
through diffusion and evaporation.

![Diffusion Simulation GIF](diffusionsimulation.gif)

## Installation

To install the dependencies use pip and the requirements.txt in this directory. e.g.

```
    $ pip install -r requirements.txt
```

## How to Run

To run the model interactively, run ``mesa runserver`` in this directory. e.g.

```
    $ mesa runserver
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Start.

## Model Parameters

There are many parameters that can be adjusted to explore different
disbursement patterns.

*  *Evaporation Rate*: the percentage of chemical that disappears each step.
*  *Diffusion Rate*: the percentage of chemical that is disbursed to surrounding cells each step.
*  *Initial Drop*: the amount of chemical dropped at the start of the simulation.

## Further Reading

Based on diffusion in the original NetLogo Ants model:

[Wilensky, U. (1997). NetLogo Ants model. http://ccl.northwestern.edu/netlogo/models/Ants. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.](https://ccl.northwestern.edu/netlogo/models/Ants)
