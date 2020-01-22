## Quickstart example
```python
from kdfconn import kdf
import pandas as pd
import gpudb
conn = gpudb.GPUdb(encoding='BINARY', host="server.ip", port="9191")
# construct instance
df = kdf(conn)
# read from csv file
df.from_pandas(pd.read_csv("tmp.csv"))
# read from kinetica table
df.read_table("tmp1")
# write to kinetica table
df.to_table("tmp2",charN_On=True, timeStampColumn="DateTime")
```
## Timestamp column
for the time stamp column, convert datetime to epoch integer column. 
for example, the load the following to pandas
```
date, time
01/01/20,  00:00
```
Then run the following to create a new timestamp column
```python
df["DateTime"] = pd.to_datetime(df['date'] + ' ' + df['time']).values.astype(np.int64) // 10 ** 6
```