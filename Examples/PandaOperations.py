import numpy as np
import pandas as pd

dataframe = pd.DataFrame({'A': [1, 2, 5, 9] * 3,
                          'B': [6, 9, 5] * 4,
                          'C': ['java', 'python', 'pandas', 'numpy', 'C', 'networks'] * 2,
                          'D': pd.Series(np.random.randint(0, 10, size=12))})

# prints the full dataframe as rows and columns
print(dataframe)
# prints the dataframe as slice
print(dataframe.iloc[1:3, 2:4])
# This sorts the values of the index 'D' and prints the dataframe as of sorted order
print(dataframe.sort_values(by='D'))
# prints the dataframe according to the given index
print(dataframe['A'])
# This will print the data types of the each column
print(dataframe.dtypes)
# This will print the starting n indices as given in parameter. By default it takes n as 5.
print(dataframe.head(7))
# This will print the last n indices as given in parameter.By default it takes n as 5.
print(dataframe.tail())
'''The following four statements prints index of the dataframe, values of the dataframe,
   describe the dataframe, transpose of the dataframe'''
print(dataframe.index)
print(dataframe.values)
print(dataframe.describe)
print(dataframe.T)
# This print the colums of the only given index with given columns
print(dataframe.loc[1:3, ['A', 'B']])
# This prints the dataframe by checking the condition given.
print(dataframe[dataframe.D > 5])
# The following two statements is nothing but printing the dataframe with following condition and by sorting the values.
df = dataframe[dataframe.D > 5]
print(df.sort_values(by='D'))
''' The following statement prints the dataframe where each element is greater than 0.
If any element is less than 0 then the element isd printed as NaN'''
print(dataframe[dataframe > 0])
'''This following two statement will add the extra column to the existing dataframe.
Make sure that length of all column should be equal '''
dataframe['E'] = [7, 5] * 6
print(dataframe)
''' This will calculate the mean of the each column of datatype int and float.
If we give 1 as parameter inside mean then it will print the mean of the each row'''
print(dataframe.mean())
''' The following two statements will split the dataframe into 3 dataframes
    and again it is concatnated into single dataframes'''
pieces = [dataframe[:3], dataframe[3:7], dataframe[7:]]
print(pd.concat(pieces))
# The following two statements will append the one more column to the dataframe.
append_row = dataframe.iloc[2]
print(dataframe.append(append_row, ignore_index=True))
# This will delete or drop the row from the dataframe. The given parameter index will be deleted
print(dataframe.drop(11))
# The following two statements used to delete the one column from the dataframe.
del dataframe['A']
print(dataframe)
# The another syntax to delete the column is to use drop statement and axis=1
print(dataframe.drop('B', axis=1))
