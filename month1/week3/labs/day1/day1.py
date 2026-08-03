# Topic: Modules, Imports & Writing Multi-File Python Programs

import math_utils
print(math_utils.add(3, 2))

# Import Specific Functions
# Instead of import math_utils, you can import the add function
from math_utils import add
print(add(3, 2))

# Import with Alias
# Aliases are common for long module names. Examples
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

import math_utils as mu
print(mu.add(3, 2))

# Import the functions and print: 7, 20, Hello, Samson!
from math_utils import add
from math_utils import multiply
from greetings import greet

print(add(3, 4))
print(multiply(5, 4))
print(greet("Samson"))
