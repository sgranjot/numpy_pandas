import pandas as pd
import numpy as np

# add some columns
df = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list(['A', 'B', 'C']))
df['D'] = df['A'] + df['C']
print(df, '\n')

# add some columns
df = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list(['A', 'B', 'C']))
df['D'] = df[['A', 'C']].sum(axis=1)
print(df, '\n')

# add all the columns
df = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list(['A', 'B', 'C']))
df['D'] = df[list(df.columns)].sum(axis=1)
print(df, '\n')

# use lambda
df = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list(['A', 'B', 'C']))
df['D'] = df.apply(lambda x: x['A'] * 100 + x['B'] / 2, axis=1)
print(df)
