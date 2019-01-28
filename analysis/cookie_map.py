import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
df = pd.read_csv('cookies.csv')
ingredients_columns = set(df.columns) - set(['Consistency (Soft, Chewy, Etc)', 'Note', 'From', 'Have I made', 
                                             'Dough Temp/Consistency', 'Shortening Flavor',"Water (Hot,Cold)", 
                                             'Butter Prep', 'Butter Type', "salt (table, fine, coarse)", "Altitude"])
print (ingredients_columns)
print (df[ingredients_columns])
for i in ingredients_columns:
   print (i, np.unique(df[i].values))

kmeans = KMeans(n_clusters=4, random_state=0).fit(df[ingredients_columns].values)
kmeans.labels_
print (kmeans.predict(df[ingredients_columns].values))
