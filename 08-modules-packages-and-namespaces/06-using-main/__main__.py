# run.py

import timing

code = '[x **2 for x in range(100_000)]'

result = timing.timeit(code, 100)
print(result)
