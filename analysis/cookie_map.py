import pandas as pd
import numpy as np

df = pd.read_csv('cookies.csv')
ingredients_columns = set(df.columns) - set(['Consistency (Soft, Chewy, Etc)', 'Note', 'From', 'Have I made', 
                                             'Dough Temp/Consistency', 'Shortening Flavor',"Water (Hot,Cold)", 
                                             'Butter Prep', 'Butter Type', "salt (table, fine, coarse)"])
print (ingredients_columns)
print (df[ingredients_columns])
for i in ingredients_columns:
   print (i)
   print (np.unique(df[i].values))


print (df["Baking Powder"])
