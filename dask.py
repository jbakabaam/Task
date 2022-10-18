# import libs
import dask.dataframe as dd
from dask.diagnostics import ProgressBar
pbar = ProgressBar()
pbar.register()

# dask dataframe
ddf = dd.read_csv('YOUR_FILE_PATH', sep=',', dtype=str, error_bad_lines=False, warn_bad_lines=False)
ddf.head()

# dask compute
res = ddf.compute(scheduler='processes', num_workers=128) # num of process
res
