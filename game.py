#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import random


# In[7]:


Capital = 10


# In[8]:


def gameA(): 
    toss = random.random() 
    #random.random() returns a uniformly distributed pseudo random floating point number in the range [0,1) (Stack overflow)
    if toss <= 0.505:
        return -1
    else:
        return 1
        


# In[9]:


def gameB():
    if Capital%3 == 0:
        toss = random.random()
        if toss <= 0.9:
            return -1
        else:
            return 1
    elif Capital%3 != 0:
        toss = random.random()
        if toss <= 0.75:
            return 1
        else:
            return -1
            


# In[ ]:


if __name__ == "__main__":
    for i in range(10):
        print(" Current Capital: ", Capital)
        choice = input("Enter A for Game A and B for Game B: ")
        if choice == 'A' or choice == 'a':
            Capital += gameA()
        elif choice == 'B' or choice == 'b':
            Capital += gameB()
        else:
            print("Invalid choice")
            break
    print("Final Capital: ", Capital)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




