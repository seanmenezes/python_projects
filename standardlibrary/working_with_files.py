from pathlib import Path
from time import ctime
import shutil
path = Path("ecommerce/__init__.py")
path.exists()
# delete it calling unlink path.unlink()
print("\n file stats", path.stat())
print("\n file st_ctime ", ctime(path.stat().st_ctime))

# path.readbytes() - read file as bytes object
# path.write_text("....")
# path.write()
print("\n file read text",path.read_text())
# above better than open
# as more steps in open
#with open("__init__.py","r") as file:
 #   pass

 # copy a file

source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

# one way
# target.write_text(source.read_text())
# a little tedious

# there is a better way cleaner and easier using shutil
shutil.copy(source,target)
