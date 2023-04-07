import os

files = os.listdir('C:\\Users\\andre\\PycharmProjects\\Studying\\RegEx')
for file in files:
    if file.endswith('.txt'):
        os.remove(file)

