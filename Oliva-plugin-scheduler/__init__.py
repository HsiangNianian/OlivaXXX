import os
from . import main

try: 
    os.mkdir(os.sep.join(['.','plugin','data','Oliva-plugin-scheduler']))
except FileExistsError: 
    pass
