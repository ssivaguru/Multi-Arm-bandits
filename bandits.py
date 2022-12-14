from random import randrange
import numpy as np, numpy.random
import random

class Bandit(object):
    def __init__(self, n) -> None:
        self.arms = n
        self.__createRewardDistribution(n)
    
    def getNoArms(self):
        return self.arms
    '''
    Create a random distribution of rewards
    '''
    def __createRewardDistribution(self, n):
        self.arm = {}
        for x in range(0, n, 1):
            distributionRange = self.__noOfDistributions()
            rangelist = np.random.dirichlet(np.ones(distributionRange),size=1)
            rewards = []
            while distributionRange != 0:
                rewards.append(randrange(1, 10))
                distributionRange = distributionRange - 1

            self.arm[x] = {}
            self.arm[x]["distri"] = np.array((rangelist[0]))
            self.arm[x]["reward"] = np.array(rewards)
            
    def __noOfDistributions(self):
        return randrange(5, 10)

    def __fibonaci_series(self, a ,b):
        return a + b
    
    def pullArm(self, armNo):
        #define pull distribution
        return random.choices(self.arm[armNo]["reward"], self.arm[armNo]["distri"])
    
    def __getExpectedVal(self):
        output = []

        for key in self.arm:
            distri = self.arm[key]["distri"]
            reward = self.arm[key]["reward"]
            temp = []
            for i in range(0, len(distri)):
                temp.append(reward[i] * distri[i])
            output.append(sum(temp))
        
        return output

    def getBestArm(self):
        out = self.__getExpectedVal()
        return np.argmax(out)
