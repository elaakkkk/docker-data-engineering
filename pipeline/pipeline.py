import sys 
import pandas as pd

month = sys.argv[1]
df = pd.DataFrame({'month': [month]})
df.to_parquet(f'./{month}.parquet', index=False)
print(df.head())