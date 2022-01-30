#!/usr/bin/env python3
# imports
import numpy as np
import matplotlib.pyplot as plt
import magpylib as magpy

# https://electronics.stackexchange.com/q/343573/6521
# https://patents.google.com/patent/US5929732

# create figure
fig = plt.figure(figsize=(8, 4))
ax1 = fig.add_subplot(121, projection='3d')  # this is a 3D-plotting-axis
ax2 = fig.add_subplot(122)  # this is a 2D-plotting-axis

d = 4
h = 4
# create magnets
s1 = magpy.source.magnet.Cylinder(mag=[0, 0, 500], dim=[d, h])
s2 = magpy.source.magnet.Cylinder(mag=[0, 0, 500], dim=[d, h])
s3 = magpy.source.magnet.Cylinder(mag=[0, 0, 500], dim=[d, h])
s4 = magpy.source.magnet.Cylinder(mag=[0, 0, 500], dim=[d, h])
s5 = magpy.source.magnet.Cylinder(mag=[0, 0, 500], dim=[d, h])

# manipulate magnets
s1.rotate(180, [0, 1, 0], anchor=[0, 0, 0])
s1.move([0, 0, h])
s2.move([0, 0, -h])
s3.rotate(90, [1, 0, 0], anchor=[0, 0, 0])
s4.rotate(-90, [1, 0, 0], anchor=[0, 0, 0])
s3.move([0, -h, 0])
s4.move([0, h, 0])
s5.rotate(-90, [0, 1, 0], anchor=[0, 0, 0])
s5.move([h, 0, 0])
# s2.move([5,0,-4])

# create collection
c = magpy.Collection(s1, s2, s3, s4, s5)

# display system geometry on ax1
magpy.displaySystem(c, subplotAx=ax1, suppress=True, direc=False)

# calculate B-field on a grid
xs = np.linspace(-30,30,59)
zs = np.linspace(-30,30,59)
Bs = np.array([[c.getB([x,0,z]) for x in xs] for z in zs])

# display field in xz-plane using matplotlib
X,Z = np.meshgrid(xs,zs)
U,V = Bs[:,:,0], Bs[:,:,2]
ax2.streamplot(X, Z, U, V, color=np.log(U**2+V**2),density=2)

plt.show()
