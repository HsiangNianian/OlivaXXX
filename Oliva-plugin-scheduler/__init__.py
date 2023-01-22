import os
from . import main

try: 
    os.mkdir(os.sep.join(['.','plugin','data','OlivaXXX']))
except FileExistsError: 
    pass
