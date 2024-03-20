import pandas as pd
from io import StringIO

city = r"""city,state
sydney,nsw
brisbane,qld
perth,sa
"""

df = pd.read_csv(StringIO(city))

df['state'] = df['state'].apply(lambda x: x.upper())
df['city'] = df['city'].apply(lambda x: x.title())
print(df)
