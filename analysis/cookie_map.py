import matplotlib
matplotlib.use('Agg')
import json
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df = pd.read_csv('cookies.csv')

#df.to_json("cookies.json", orient='index')
df_json_pretty = json.dumps(json.loads(df.to_json(orient='records')), indent=2, sort_keys=True)
f = open('cookies.json', 'w')
f.write(df_json_pretty)
f.close()
exit()
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
centers = kmeans.cluster_centers_
print (centers)
for i in range(len(ingredients_columns)-1):
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
    plt.scatter(df[ingredients_columns].values[:,i], df[ingredients_columns].values[:,i+1], cmap='viridis')
    plt.savefig('centers_' + str(i) + '.png')
    plt.clf()
