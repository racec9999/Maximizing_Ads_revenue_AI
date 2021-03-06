#Cesar Arcos : cesar99ag@gmail.com

# Maximizing the Revenues of an Online Retail Business with Thompson Sampling

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import random

# Setting the parameters
N = 10000 #total number of users 1n = 1user
d = 9

# Creating the simulation
conversion_rates = [0.05,0.13,0.09,0.16,0.11,0.04,0.20,0.08,0.01]
#Creating the simulated matrix
X = np.array(np.zeros([N,d]))
for i in range(N):#rows
    for j in range(d):#columns
        if np.random.rand() <= conversion_rates[j]:
            X[i,j] = 1

# Implementing a Random Strategy and Thompson Sampling
strategies_selected_rs = []
strategies_selected_ts = []
total_reward_rs = 0
total_reward_ts = 0
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
for n in range(0, N):
    # Random Strategy
    strategy_rs = random.randrange(d)#we selcected a random strtategy for the add 
    strategies_selected_rs.append(strategy_rs)
    reward_rs = X[n, strategy_rs]#we selected the rewards form the matrix we have created before 
    total_reward_rs += reward_rs
    # Thompson Sampling
    strategy_ts = 0
    max_random = 0
    for i in range(0, d):#loop over strategies
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)#we create our own distribution for each strategie
        if random_beta > max_random:
            max_random = random_beta
            strategy_ts = i
    reward_ts = X[n, strategy_ts]
    if reward_ts == 1:
        numbers_of_rewards_1[strategy_ts] += 1
    else:
        numbers_of_rewards_0[strategy_ts] += 1
    strategies_selected_ts.append(strategy_ts)
    total_reward_ts = total_reward_ts + reward_ts

# Computing the Absolute and Relative Return
absolute_return = (total_reward_ts - total_reward_rs) * 100 #amount per user 100/year
relative_return = (total_reward_ts - total_reward_rs) / total_reward_rs * 100
print("Absolute Return for 10000 users: {:.0f} $".format(absolute_return))#the amount of $ will earn thanks to thompson sampling 
print("Relative Return for 10000 users: {:.0f} %".format(relative_return))

# Plotting the Histogram of Selections
plt.hist(strategies_selected_ts)
plt.title('Histogram of Selections')
plt.xlabel('Strategy')
plt.ylabel('Number of times the strategy was selected')
plt.show()
