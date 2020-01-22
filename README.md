# Example
```python
from kdfconn import kdf
import pandas as pd
import gpudb
conn = gpudb.GPUdb(encoding='BINARY', host="server.ip", port="9191")

# construct instance
df = kdf(conn)
# read from csv file
df.from_pandas(pd.read_csv("./tmp/tmp.test3.csv"))
# read from kinetica table
df.read_table("est6")
# write to kinetica table
df.to_table("est15",charN_On=True, timeStampColumn="ValidDateTime")
```