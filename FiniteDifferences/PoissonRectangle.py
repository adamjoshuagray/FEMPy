"""
    This is just a little sample script which solves the poisson equation on a rectangle
    using finite differences. 
    This is essentially the simplest pde solver in the codebase.
    
    Written by Adam J. Gray
    github: github.com/adamjoshuagray
"""

import numpy as np
import scipy.linalg as la
import math
import pylab as plot
from mpl_toolkits.mplot3d import Axes3D

width       = 1.2
height      = 1.2
h_x         = 0.2
h_y         = 0.2


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

num_x       = int( round( width / h_x - 2 ) )
num_y       = int( round( height / h_y - 2 ) )
num_U       = num_x * num_y

def to_pair_index(i): return ( int( math.floor( i / num_x ) ), int( i % num_x ) )
def to_single_index(i,j): return i * num_x + j

L           = np.diag( np.repeat( 1.0, num_U ) )

"""
    Setup the main matrix.
    This section here could be vectorized.
"""

for i in range( num_x ):
    for j in range( num_y ):
        if i != 0:
            L[ to_single_index( i, j ), to_single_index( i - 1, j ) ] = -h_x / h_y * 0.25
        if i != num_y - 1:
            L[ to_single_index( i, j ), to_single_index( i + 1, j ) ] = -h_x / h_y * 0.25
        if j != 0:
            L[ to_single_index( i, j ), to_single_index( i, j - 1 ) ] = -h_y / h_x * 0.25
        if j != num_x - 1:
            L[ to_single_index( i, j ), to_single_index( i, j + 1 ) ] = -h_y / h_x * 0.25

"""
    Setup the boundry values.
"""

a           = np.repeat( 0.25, 2 * ( num_x + num_y ) )
b           = np.concatenate( ( np.repeat( 1., num_x ), np.repeat( 0., num_x + 2 * num_y ) ) )
c           = a * b

u           = la.solve( L, c )
U           = u.reshape( ( num_x, num_y ) )

"""
    Plot the result.
"""

fig         = plot.figure()
ax          = Axes3D( fig )
x           = np.arange( 0, width, h_x )[ 1: -1 ]
y           = np.arange( 0, height, h_y )[ 1 : -1 ]
x, y        = np.meshgrid( x, y )
ax.plot( x, y, U, rstride=1, cstride=1, cmap='hot' );
