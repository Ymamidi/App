import pandas as pd
from pandas.io.json import json_normalize
import json

with open('C:/Personal_Projects/Development/Tarun/SL126745_results.json') as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
# df.to_csv(r'C:/Personal_Projects/Development/Tarun/File.csv', index = False)

# df1= pd.DataFrame.from_dict(df["seq_info"], orient='columns')
# df = pd.DataFrame(list(df['seq_info']))

s = pd.DataFrame.from_dict(df['seq_info'].to_dict())

data1 = pd.read_csv (r'C:/Personal_Projects/Development/Tarun/try.csv')
df2 = data1.F2.str.split(',').apply(pd.Series) 
print(df2)
# print(data1)
# data1.assign(F1=df.F1.str.split(","))

# print(s)
# print(pd.DataFrame(list(s[0])))
# df = pd.DataFrame(df1)
# print(df)