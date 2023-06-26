import pathlib
import inspect
from pathology.path import Path


script_dir = pathlib.Path(__file__).parent.resolve()
print(script_dir)
print(str(Path.script_dir()/'file.txt'))
