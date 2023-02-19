import random
import numpy as np


class NeuralNetwork():

    def __init__(self, layer_sizes):

        self.Ws = ['_']
        self.bs = ['_']

        for k in range(1, len(layer_sizes)):
            tmp = []
        
        # Create a uniform random array of -1 to 1 for Ws
            for i in range(layer_sizes[k]):
                row = []
                for j in range(layer_sizes[k-1]):
                    row.append(random.uniform(-1, 1))
                tmp.append(row)
                
        # For First time Bs is a zero array
            self.bs.append(np.zeros((layer_sizes[k], 1)))

            self.Ws.append(np.array(tmp))
            
    def activation(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, x):
        
        tmp_layer = x 

        for i in range(1, len(self.Ws)):
            tmp_layer = self.activation((self.Ws[i] @ tmp_layer) + self.bs[i])
        
        return tmp_layer

