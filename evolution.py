import os
import random
import numpy as np

from player import Player
from copy import deepcopy
from config import CONFIG


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # Mutate the Child
        # The rate of mutate must be high becuase of i just use mutate not crossover
        # Because we mutate allmost everything the changeing rate is low
        if random.random() < 0.7:
            
            for b in child.nn.bs:
                if b == '_':
                    continue
                b += np.random.normal(0, 0.03, b.shape)

            for W in child.nn.Ws:
                if W == '_':
                    continue
                W += np.random.normal(0, 0.03, W.shape)
        
        return child


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # Just pass prev_player to next_population_selection and after that mutate that
            new_players = self.next_population_selection(prev_players, num_players)
            new_players = [self.mutate(deepcopy(i)) for i in new_players]
            return new_players

    def next_population_selection(self, players, num_players):

        # Calculate probabilities form fitness and pass it to np.random.choice use Roulette Wheel
        record_file = open("record.txt","a")
        probabilities = []
        sum = 0
        
        for i in players:
            probabilities.append(i.fitness)
            sum += i.fitness

        record_file.write(str(min(probabilities)))
        record_file.write(" ")
        record_file.write(str(sum/len(probabilities)))
        record_file.write(" ")
        record_file.write(str(max(probabilities)))
        record_file.write("\n")       
        record_file.close()

        for i in range(len(probabilities)):
            probabilities[i] /= sum

        tmp = np.random.choice(players, num_players, p=probabilities, replace=False)
        next_pop = list(tmp)
        return next_pop