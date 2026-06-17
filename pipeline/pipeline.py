import sys
import pandas as pd
print("arguments", sys.argv)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

df = pd.DataFrame({'day': [day]})
df.to_parquet(f'./{day}.parquet', index=False)
print(df.head())