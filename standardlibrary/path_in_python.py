from pathlib import Path

Path("/usr/local/bin")
Path()
path  = Path("ecommerce/__init__.py")
Path() / "ecommerce" / "__init__.py"
print("Path home ",Path.home())
print("\n path exists",path.exists())
print("\n path is file ",path.is_file())
print("\n path is dir ",path.is_dir())
print("\n path name ",path.name)
print("\n path stem ",path.stem)
print("\n path suffix ",path.suffix)
print("\n path parent ",path.parent)
path = path.with_name("file.txt")
print(path)
print("\n path absolute ",path.absolute())



