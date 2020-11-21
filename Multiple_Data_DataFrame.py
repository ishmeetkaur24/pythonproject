
import pandas as pd
import numpy as np

myData = {
    'name':['Xavier','Ann','Jana','Yi','Robin','Amal','Nori'],
    'City': ['US','Sudbury','Prague','Shanghai','Manchester','Ciaro','Osaka'],
    'age':[41,28,33,34,38,31,37],
    'py-score':[88.0,79.0,81.0,80.0,68.0,61.0,84.0]
}


row = [101,102,103,104,105,106,107]

df = pd.DataFrame(data= myData , index =row)
print(df)

print(df.head(n=2))
print("Last five values from DataFrame")
print(df.tail(n=5))

MyCities = df['City']
print(MyCities)