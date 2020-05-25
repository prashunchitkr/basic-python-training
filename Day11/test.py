# importing numpy which we installed using pip in our venv
import numpy as np
# see Day8 files for importing packages and modules

# creating sample array using numpy method
array_1 = np.arange(5)
array_2 = np.arange(5)

add = array_1 + array_2

print('{} + {} = {}'.format(array_1, array_2, add))