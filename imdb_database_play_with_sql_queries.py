# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:17:25 2019
IMDB DATABASE PLAY WITH PYTHON SQL QUERIES
@author: omerzulal
"""

import sqlite3 as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
plt.close("all")
plt.style.use("seaborn-pastel")

#%% CREATING THE DATABASE (.DB) CREATING ITS TABLES
import os

tsv_path = r"C:\Users\omerzulal\Downloads\IMDB Databases"

conn = sql.connect(tsv_path+"\\"+"imdb_database.db")
c = conn.cursor()

filenames = os.listdir(tsv_path)
filenames = pd.Series(filenames)[[i.endswith(".tsv") for i in filenames]].reset_index(drop=True)

#table fields are taken from the imdb database webpage
table_fields = {"name_basics":["nconst text","primaryName text","birthYear int","deathYear int","primaryProfession text","knownForTitles text",],
                "title_akas":["titleId  text","ordering int","title int","region int","language text","types text","attributes text","isOriginalTitle int"],
                "title_basics":["tconst text","titleType text","primaryTitle text","originalTitle text","isAdult int","startYear int","endYear int","runtimeMinutes int","genres text"],
                "title_crew":["tconst text","directors text","writers text"],
                "title_principals":["tconst text","oredering int","nconst text","category text","job text","characters text"],
                "title_ratings":["tconst text","averageRating real","numVotes integer"]
                }

# creates tables, reads tsv files generates dataframes and insert it into the database
# it should take around 5 minutes to complete
for file in filenames:
    print(file)
    t1 = time.time()
    temp_path = r"C:\Users\omerzulal\Downloads\IMDB Databases\%s"%(file)
    with open(temp_path) as f:
        pd.read_csv(temp_path,delimiter="\t").to_sql(file[:-4],conn)  
    conn.commit()
    print("Query Succeeded in %.2f seconds"%(time.time()-t1))
conn.close()      

#%% YEARLY ANALYSIS OF NUMBER OF VOTERS, AVERAGE RATING AND VOTERS PER FILM
path = r"C:\Users\omerzulal\Downloads\IMDB Databases\imdb_database.db"

#create a connection to the database
conn = sql.connect(path)

query = '''
select title_basics.startYear as "Year", 
	count(*) as "Number of Films", 
	sum(numVotes) as "Number of Film Voters", 
	round(avg(numVotes),0) as "Average Voters Per Film", 
	round(avg(averageRating),2) as "Average Film Rating"
from title_ratings
join title_basics on title_basics.tconst=title_ratings.tconst
where startYear is not "\\N" and titleType is "movie" and startYear<2018
group by title_basics.startYear order by title_basics.startYear;
'''
#run the sql query using pandas function and store it into a dataframe
df = pd.read_sql_query(query,conn)

df.Year = pd.to_numeric(df.Year)
#%% Process the data
x1 = df["Year"][df["Number of Film Voters"].idxmax()]
y1 = df["Number of Film Voters"].max()

x2 = df["Year"][df["Average Voters Per Film"].idxmax()]
y2 = df["Average Voters Per Film"].max()

#%% scale(normalise) the data and keep original
from sklearn import preprocessing
df_norm = pd.DataFrame(preprocessing.scale(df),columns=df.columns)
df_norm["Year"] = df["Year"]

#%% subplot show original values

fig = plt.figure(figsize=(5,10))
fig.subplots_adjust(hspace=0.57)
ax1 = plt.subplot(411)
ax2 = plt.subplot(412)
ax3 = plt.subplot(413)
ax4 = plt.subplot(414)

ax1.plot(df.Year,df["Number of Films"])
ax1.set_title("Number of Films",fontweight="bold",fontsize=10)

ax2.plot(df.Year,df["Number of Film Voters"])
ax2.set_title("Number of Film Voters",fontweight="bold",fontsize=10)
ax2.annotate(x1,xy=(x1,y1),xytext=(x1-50,y1*0.7),
             arrowprops=dict(arrowstyle="fancy"))

ax3.plot(df.Year,df["Average Voters Per Film"])
ax3.set_title("Average Voters Per Film",fontweight="bold",fontsize=10)
ax3.annotate(x2,xy=(x2,y2),xytext=(x2-50,y2*0.7),
             arrowprops=dict(arrowstyle="fancy"))

ax4.plot(df.Year,df["Average Film Rating"])
ax4.set_title("Average Film Rating",fontweight="bold",fontsize=10)

#%% show normalised values
df_norm.plot(x="Year")

#%% CORRELATION BETWEEN FILM DURATION, RATING, AND NUMBER OF VOTES

query = """
select averageRating, numVotes, title_basics.runtimeMinutes from title_ratings
join title_basics on title_basics.tconst=title_ratings.tconst
where title_basics.titleType is "movie" and title_basics.runtimeMinutes is not "\\N";
"""

#create a connection to the database
conn = sql.connect(path)

t1 = time.time()
#run the sql query using pandas function and store it into a dataframe
df = pd.read_sql_query(query,conn)
print("It took %.1f seconds"%(time.time()-t1))

df.runtimeMinutes = pd.to_numeric(df.runtimeMinutes)

df2 = df.copy()
df = df2[df2.numVotes>5000]

dur_bins = np.arange(0,205,5)
df_gr_by_film_dur = df.groupby(pd.cut(df.runtimeMinutes,dur_bins)).mean()

plt.figure(figsize=(5,8))
plt.gcf().subplots_adjust(hspace=0.46,left=0.21)

plt.subplot(211)
#plt.bar(dur_bins[:-1],df_gr_by_film_dur.averageRating,width=5)
plt.plot(dur_bins[:-1],df_gr_by_film_dur.averageRating,"o-",markerfacecolor="None")
plt.xlabel("Film Duration (minutes)")
plt.ylabel("Average Rating (IMDB)")
plt.title("Film Ratings vs Runtime",fontweight="bold")
plt.xlim([80,dur_bins[-1]])
plt.grid(linestyle=":")

plt.subplot(212)
#plt.bar(dur_bins[:-1],df_gr_by_film_dur.numVotes,width=5)
plt.plot(dur_bins[:-1],df_gr_by_film_dur.numVotes,"o-",markerfacecolor="None")
plt.xlabel("Film Duration (minutes)")
plt.ylabel("No. of Voters (IMDB)")
plt.title("Average No. of Voters vs Runtime",fontweight="bold")
plt.grid(linestyle=":")
plt.xlim([80,dur_bins[-1]])      
