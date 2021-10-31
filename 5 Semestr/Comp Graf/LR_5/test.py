import numpy as np
from myplot import plot_verticles

vertices = np.array(
    [
        [-3, -3, 0],
        [+3, -3, 0],
        [+3, +3, 0],
        [-3, +3, 0],
        [+0, +0, +3]
    ]
)

plot_verticles(vertices = vertices, isosurf = False)