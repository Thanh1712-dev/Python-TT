import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
def heart_3d(x,y,z):
    return (x**2+(9/4)*y**2+z**2-1)**3-x**2*z**3-(9/80)*y**2*z**3
 
def plot_implicit(fn,bbox=(-1.5,1.5)):
    xmin,xmax,ymin,ymax,zmin,zmax = bbox*3
    fig = plt.figure('HEART')
    ax = fig.add_subplot(111,projection = '3d')
    A = np.linspace(xmin,xmax,80)
    B = np.linspace(xmin,xmax,30)
    A1,A2 = np.meshgrid(A,A)
 
    for z in B:
        X,Y = A1,A2
        Z = fn(X,Y,z)
        cest = ax.contour(X,Y,z+Z,[z],zdir='z',colors=('r',))
 
    for y in B:
        X,Z = A1,A2
        Y = fn(X,y,Z)
        cest = ax.contour(X,Y+y,Z,[y],zdir = 'y',colors = ('red',))
 
    for x in B :
        Y,Z=A1,A2
        X = fn(x,Y,Z)
        cest = ax.contour(X+x,Y,Z,[x],zdir = 'x',colors = ('red',))
 
    ax.set_zlim3d(zmin,zmax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)
        
    plt.show()
 
if __name__=='__main__':
    plot_implicit(heart_3d)
