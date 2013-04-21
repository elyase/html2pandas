from pyquery import PyQuery as pq
from pandas import DataFrame
import numpy as np

def convert(html):
    d = pq(html)
    columns = d('thead tr').eq(0).text().split()
    #index_columns = d('thead tr').eq(1).text().split()
    n_rows = len(d('tbody tr'))
    values = np.array(d('tbody tr td').text().split()).reshape(n_rows, len(columns))
    return DataFrame(values, columns=columns)
