# A-Very-Simple-Deep-Q-Learning-Library-I-Made-From-Scratch
A horrible deep q-learning algorithm that uses my neural network library I also made from scratch.

This program is fairly simple, it creates an "agent" object that can be used in simple reinforcement learning environments.

An "agent" object has a "history" and a "brain". The "brain" is a "network" object created by my "NeuralNetworkV6" program with the structure determined by the list "lis". For more information on what the "lis" list is used in the creation of the "brain", please read the "please read" file in my neural network repository. The "history" is a list meant to store the previous state of the agent.
example:
a = agent([2,3,1])        #This creates a q-learning agent with a neural network structure of 2 nodes x 3 nodes x 1 node.

The "q" function is literally the q-function for the algorithm. It takes the agent's current state as the input, and outputs the q value of each action(each output node corresponds to a possible action).

The "newq" function trains the neural network of the agent depending on its current state, it reward, the learning rate, and the discount factor. It is based on the Bellman equation.

the "reset" function simply clears the "history" list to make sure the agent doesn't have access to stray data when being reset.
