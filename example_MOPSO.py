from platypus.algorithms import ParticleSwarm
from platypus.operators import TournamentSelector, PM, SBX, GAOperator
from platypus.problems import DTLZ2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

problem = DTLZ2(3)

algorithm = ParticleSwarm(problem,
                   population_size = 100,
                   selector = TournamentSelector(2),
                   variator = GAOperator(SBX(1.0), PM(1.0 / problem.nvars)))

algorithm.run(10000)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([s.objectives[0] for s in algorithm.result],
           [s.objectives[1] for s in algorithm.result],
           [s.objectives[2] for s in algorithm.result])
plt.show()