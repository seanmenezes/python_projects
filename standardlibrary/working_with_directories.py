from pathlib import Path
path = Path("ecommerce")
#path.exists()
#path.mkdir()
#path.rmdir()
#path.rename("ecommerce2")
print("\n path iterdir()",path.iterdir())


for p in path.iterdir():
    py_files = [p for p in path.glob("*.py")]
    print(py_files)

# list comprehension
paths = [p for p in path.iterdir() if p.is_dir()]
path.glob("*.py")
print(paths)

for p in path.iterdir():
    py_files = [p for p in path.rglob("*.py")]
    print(py_files)