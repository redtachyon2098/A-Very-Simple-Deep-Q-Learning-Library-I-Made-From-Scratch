#Deep Q learning attempt- using a neural network as the q function
#Bellman equation:  new q = (old q) + (learning rate) * ( (reward) + (discount factor) * (future reward estimate) - (old q))
import NeuralNetworkV6 as nn

import random as r

def biggest(lis):
    big = [0]
    for x in range(len(lis) - 1):
        y = x + 1
        if(lis[y] > lis[big[0]]):
            big = [y]
        if(lis[y] == lis[big[0]] and big[0] != y):
            big.append(y)
    return big[r.randint(0,len(big) - 1)]

class agent:
    def __init__(self,brain):
        self.brain = nn.network(brain) #I'm using this network as the q function
        self.history = []

    def q(self,state):
        self.brain.predict(state)
        self.history = state
        a = self.brain.output()
        return a

    def newq(self,state,reward,LearnRate,DiscountFactor):
        OldState = self.history
        self.brain.predict(OldState)
        oldQ = self.brain.output()
        self.brain.predict(state)
        FutureMaxQ = biggest(self.brain.output())
        bellman = []
        for x in range(len(oldQ)):
            bellman.append(oldQ[x] + LearnRate * (reward[x] + DiscountFactor * FutureMaxQ - oldQ[x]))
        self.brain.train([OldState],[bellman],LearnRate,10)

    def reset(self):
        self.history = []
