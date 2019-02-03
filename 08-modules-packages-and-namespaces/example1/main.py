import sys

print('===============================')
print('Running main.py - module name: {0}'.format(__name__))

import module1 # note: module code is executed when the import line is reached, and is then cached in sys

print(module1)

module1.pprint_dict('main.globals', globals())

print(sys.path) # python looks for the module in the path
print(sys.modules['module1'])


print('importing module1 again...')
import module1 # note: the module1 code is not executed again, because it is already cached from prev import
# we could delete module1 from our global namespace and reimport, but because it is cached in sys modules, it would 
# just use the cache and add it back to the global namespace

print('===============================')