# password = "⨀⨑⨖⨟⨢⨡⨞⨛ĤěĪĪó123321'sWorld000"
# new = "ÂBĈ098765__4321Hello's()*&^"
# bb = 'HI1q4RFwpNxWq7Re'


from collections import deque
import random
import os
from pathlib import *
import shutil
import sys
import re
import getopt
from itertools import cycle
import subprocess
import csv


with open('file.csv', 'w', encoding='utf-8-sig') as file:
    fieldnames = ['Source_path', 'Dst_path', 'Enc_type', 'Mode', 'Key']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
