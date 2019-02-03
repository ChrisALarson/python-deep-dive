# main.py
import os.path
import types
import sys

# we are going to manually import module1
module_name = 'module1'
module_file = 'module1_source.py'
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

# read source code from file
with open(module_abs_file_path, 'r') as code_file:
    source_code = code_file.read()

# create a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# set a reference in sys.modules
sys.modules[module_name] = mod

# compile the source code
code = compile(source_code, filename=module_abs_file_path, mode='exec')

# execute compiled source code
exec(code, mod.__dict__) # add objects from executing code to mod.__dict__ namespace

# DONE!

# running from mod namespace
mod.hello()

# running from sys modules cache
import module1
module1.hello()
