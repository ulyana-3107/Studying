import os
from os import listdir

for p in listdir('C:\\Users\\andre\\PycharmProjects\\Studying'):
    if p.endswith('txt'):
        os.remove('C:\\Users\\andre\\PycharmProjects\\Studying\\' + p)

