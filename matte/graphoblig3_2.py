import numpy as np
import math

matriseA = np.array([
            [2, 1-math.sqrt(5), 0,0],
            [(1-math.sqrt(5)), ((3-math.sqrt(5))/2), 0,1],
            [0,0,((1+math.sqrt(5))/2),0],
            [0,1,0,1],
            ])
print(matriseA)
print()

eigenverdier, vektor = np.linalg.eig(matriseA)
print(eigenverdier)

