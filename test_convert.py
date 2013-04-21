from pandas import DataFrame
import numpy as np
from html2pandas import convert

def test_convert():
    df = DataFrame(np.random.rand(4,5), columns = list('abcde'))
    assert np.allclose(convert(df.to_html(), float), df, rtol=1e-4)
