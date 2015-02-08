"""
    This is just a little sample script which solves the poisson equation on a rectangle
    using finite differences. 
    This is essentially the simplest pde solver in the codebase.
    
    Written by Adam J. Gray
    github: github.com/adamjoshuagray
"""

import numpy as np

width       = 10
height      = 10
h_x         = 0.01
h_y         = 0.01

""" 
    We need a standard indexation of grid points. 
    We use the following layout
    
    0    1    2    3    4    5
    6    7    8    9    10   11
    12   13   14   15   16   17
    ...
    
    Which would correspond to
    0,0  0,1  0,2  0,3  0,4  0,5
    1,0  1,1  1,2  1,3  1,4  1,5
    2,0  2,1  2,2  2,3  2,4  2,5
    ...
    
    And as the boundary values are known
    then only the interior points are
    undetermined.
"""

diagonal_block = np.array( [ [1,-0.25, 0], [-0.25,1,-0.25], [0,-0.25, 1] ] )

print( "asd" )


