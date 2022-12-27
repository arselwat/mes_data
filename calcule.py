import pandas as pd
df = pd.DataFrame(columns = ['A', 'B', 'C'])
df
df.loc[0, 'A'] = 1
df.loc[1] = [2, 3, 4]
print(df)
b= pd.loc[1]
print(b)