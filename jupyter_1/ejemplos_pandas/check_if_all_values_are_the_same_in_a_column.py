import pandas as pd
from io import StringIO

str_data = r"""
date,weather
2018-03-04,sunny
2018-03-05,sunny
2018-03-06,sunny
"""
df = pd.read_csv(StringIO(str_data))

assert (df['weather'] == 'sunny').all(), "Values are not the same in the column"