# html2pandas
Small function to recover a pandas Dataframe from its html representation.

## Usage:
```python
from html2pandas import convert

df = DataFrame(np.random.rand(4,5), columns = list('abcde'))
convert(df.to_html(), float)
```

## Requirements

pyquery
numpy
pandas

## Update:

Since version 0.12 pandas has the function [read_html] (http://pandas.pydata.org/pandas-docs/stable/generated/pandas.io.html.read_html.html?highlight=read_html#pandas.io.html.read_html).
