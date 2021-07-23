#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
class Nine_Coins:
    def __init__(self, possibility):
        self.possibility = possibility
        kstr = ''
        wstr = ''
        for i in range(9):
            k = possibility % 2
            possibility //= 2
            kstr += str(k)

            if k == 0:
                wstr += 'H'
            else:
                wstr += 'T'
        self.kstr = kstr
        self.wstr = wstr

    def __str__(self):
        return f'binary: {self.kstr[::-1]} and decimal: {self.possibility}'
  
    def __repr__(self):
        return f'Nine_Coins: {self.wstr[::-1]}'
    
    def toss(self):
        self.possibility = random.randint(1, 512)
        possibility = self.possibility
        kstr = ''
        wstr = ''
        for i in range(9):
            k = possibility % 2
            possibility //= 2
            kstr += str(k)

            if k == 0:
                wstr += 'H'
            else:
                wstr += 'T'
        self.kstr = kstr
        self.wstr = wstr

