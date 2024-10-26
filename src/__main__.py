from pkg import *
from lib import *

"""

## Parse command line arguments.

#### CLI argument examples:

python filelistup.py -prefix="~\music" -extension="mp3"

"""
args = parseargs()
filelist = listup(PATH(args['prefix']), args['extension'])
for file in filelist:
    sys.stdout.write(str(file)+'\n')
    sys.stdout.flush()
sys.exit(0)