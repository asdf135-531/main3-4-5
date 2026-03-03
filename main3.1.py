import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class direct:
    def __init__ (self,x0,y0,z0):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
    def direct(self):
        while True:
            l = random.uniform(-1, 1)
            n = random.uniform(-1, 1)
            m = random.uniform(-1, 1)
            len = (l ** 2 + m ** 2 + n ** 2) ** 0.5
            if len < l:
                break
            l=l/len
            n=n/len
            m=m/len
            return l,n,m
    def plot(self, x, y, z):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

d=direct(0,0,0)
x = []
y = []
z = []
for _ in range(10000):
    l,n,m=d.direct()
    x.append(l + d.x0)
    y.append(n + d.y0)
    z.append(m + d.z0)
d.plot(x,y,z)