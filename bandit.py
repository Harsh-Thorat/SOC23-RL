#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import matplotlib.pyplot as plt


# In[19]:


actions = [
    lambda: np.random.normal(2, 1),     # Gaussian distribution
    lambda: np.random.choice([5, -6]),  # Fair coin toss
    lambda: np.random.poisson(2),       # Poisson distribution
    lambda: np.random.exponential(3),   # Exponential distribution
    lambda: np.random.choice([actions[i]() for i in range(4)], p=[0.25, 0.25, 0.25, 0.25])  # The crazy button
]


# In[20]:


def epsilon_greedy(epsilon, Q, N, episode_steps):
    rewards = []
    for episode in range(1, episode_steps + 1):
        episode_rewards = 0
        for t in range(1, 101):
            if np.random.random() < epsilon:
                action = np.random.choice(range(5))
            else:
                action = np.argmax(Q)
            #explore or exploit

            reward = actions[action]()  
            episode_rewards += reward

            # Updating action value estimates and action counts
            N[action] += 1
            Q[action] += (reward - Q[action]) / N[action]

        rewards.append(episode_rewards)

    return rewards


# In[21]:


# Setting parameters
episode_steps = 100
epsilon_values = [0.1, 0.01, 0] 


# In[22]:


rewards_curves = []
for epsilon in epsilon_values:
    Q = np.zeros(5)  # Action value estimates
    N = np.zeros(5)  # Action counts
    rewards = epsilon_greedy(epsilon, Q, N, episode_steps)
    rewards_curves.append(rewards)


# In[23]:


x = np.arange(1, episode_steps + 1)
labels = ['Epsilon = 0.1', 'Epsilon = 0.01', 'Epsilon = 0']

plt.figure(figsize=(10, 6))
for rewards, label in zip(rewards_curves, labels):
    plt.plot(x, rewards, label=label)

plt.xlabel('Episode')
plt.ylabel('Reward at the end of episode')
plt.legend()
plt.title('Epsilon-Greedy Agent Performance')
plt.show()


# In[ ]:





# In[ ]:




