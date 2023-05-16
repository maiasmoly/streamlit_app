import pandas as pd
import numpy as np

rng = np.random.default_rng(123)

d = (rng.random((3, 3)))
print(pd.DataFrame(data = d))
