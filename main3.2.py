import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class direct:
    def __init__ (self,x0,y0,z0):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
    def direct(self):
        phi = math.pi*random.uniform(-1,1)
        teta = math.acos(2*random.uniform(0, 1)-1)
        return phi,teta
    def plot(self, x, y, z):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
d=direct(0,0,0)
x =[]
y =[]
z =[]
for _ in range(1000):
    phi,teta=d.direct()
    r=1
    x.append(d.x0+r*math.sin(teta)*math.cos(phi))
    y.append(d.y0+r*math.sin(teta)*math.sin(phi))
    z.append(d.z0+r*math.cos(teta))
d.plot(x,y,z)