import pandas as pd
import numpy as np

series = pd.Series([1, 2, 65, 98, 14, 25, np.nan])
# print(series)
#
dates = pd.date_range('20130101', periods=12)
# print(dates)
#
df = pd.DataFrame(np.random.randn(12, 4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
# print(df2.dtypes)
#
#
# print("Head", df2.head(2))
#
# print(df2.tail(3))
#
# print("Index is", df.index)
# print(df.columns)
# print(df.values)
# print(df.describe)
# print(df.T)
# print(df.sort_index(axis=1, ascending=False))
#
#
