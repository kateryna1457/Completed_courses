import pyarrow.parquet as pq
import pandas

table = pq.read.table('taxi.parquet')
df = table.to_pandas()