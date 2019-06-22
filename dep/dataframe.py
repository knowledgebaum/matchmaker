#https://thispointer.com/python-pandas-how-to-convert-lists-to-a-dataframe/

import pandas as pd
from list_chunk import matches, x


# Creating a dataframe object from listoftuples
dfObj = pd.DataFrame(x)
print(dfObj)

dfObj.to_csv(path_or_buf='CSV_output_.csv')
