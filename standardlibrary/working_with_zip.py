from pathlib import Path
from zipfile import ZipFile
# create zip file
#with  ZipFile("files.zip","w") as zip:
   # for path in Path("ecommerce").rglob("*.*"):
        #zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print("\n info.file_size",info.file_size)
    print("\n info.compress_size",info.compress_size)
    print("\n info.filename",info.filename)
    print("\n info.create_version",info.create_version)
    print("\n info.extract_version",info.extract_version)
    zip.extractall("extract")