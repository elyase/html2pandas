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