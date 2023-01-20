import os
from . import main
from . import github

try: 
    os.mkdir(os.sep.join(['.','plugin','data','OlivaGithub']))
except FileExistsError: 
    pass