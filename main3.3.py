import random
import matplotlib.pyplot as plt
class source:
    def __init__ (self,m):
        self.m = m #число энергетических линий
    def energy(self,k): #К - число исследуемых частиц
        p=[]
        E=[]
        N=[]
        p.append(random.randint(0, 10))
        E.append(random.uniform(0, 10))
        N.append(0)
        for i in range(1,self.m):
            p.append(random.randint(p[i-1], p[i-1]+10))
            E.append(random.uniform(E[i-1]+1, E[i-1]+10))
            N.append(0)
        for _ in range(k):
            rand_numb = random.randint(0, p[self.m-1])
            i=0
            while(0==0):
                if rand_numb <= p[i]:
                    N[i]+=1
                    break
                else:
                 i+=1
        plt.bar(E,N)
        plt.show()
s1=source(5)
s1.energy(10000)
s2=source(10)
s2.energy(10000)
s3=source(100)
s3.energy(10000)