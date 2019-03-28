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
#%% YEARLY ANALYSIS OF NUMBER OF VOTERS, AVERAGE RATING AND VOTERS PER FILM

##path = r"C:\Users\omerzulal\Downloads\IMDB Databases\imdb_db_all.db"
#path = r"C:\Users\omer.eker\Downloads\IMDB Databases\imdb_db_all.db"
#
##create a connection to the database
#conn = sql.connect(path)
#
##run the sql query using pandas function and store it into a dataframe
#df = pd.read_sql_query(query,conn)

#query = '''
#select title_basics.startYear as "Year", 
#	count(*) as "Number of Films", 
#	sum(numVotes) as "Number of Film Voters", 
#	round(avg(numVotes),0) as "Average Voters Per Film", 
#	round(avg(averageRating),2) as "Average Film Rating"
#from title_ratings
#join title_basics on title_basics.tconst=title_ratings.tconst
#where startYear is not "\\N" and titleType is "movie" and startYear<2018
#group by title_basics.startYear order by title_basics.startYear;
#'''

##%% Process the data
#x1 = df["Year"][df["Number of Film Voters"].idxmax()]
#y1 = df["Number of Film Voters"].max()
#
#x2 = df["Year"][df["Average Voters Per Film"].idxmax()]
#y2 = df["Average Voters Per Film"].max()
#
##%% scale(normalise) the data and keep original
#from sklearn import preprocessing
#df_norm = pd.DataFrame(preprocessing.scale(df),columns=df.columns)
#df_norm["Year"] = df["Year"]
#
##%% subplot show original values

#fig = plt.figure(figsize=(5,10))
#fig.subplots_adjust(hspace=0.57)
#ax1 = plt.subplot(411)
#ax2 = plt.subplot(412)
#ax3 = plt.subplot(413)
#ax4 = plt.subplot(414)
#
#ax1.plot(df.Year,df["Number of Films"])
#ax1.set_title("Number of Films",fontweight="bold",fontsize=10)
#
#ax2.plot(df.Year,df["Number of Film Voters"])
#ax2.set_title("Number of Film Voters",fontweight="bold",fontsize=10)
#ax2.annotate(x1,xy=(x1,y1),xytext=(x1-50,y1*0.7),
#             arrowprops=dict(arrowstyle="fancy"))
#
#ax3.plot(df.Year,df["Average Voters Per Film"])
#ax3.set_title("Average Voters Per Film",fontweight="bold",fontsize=10)
#ax3.annotate(x2,xy=(x2,y2),xytext=(x2-50,y2*0.7),
#             arrowprops=dict(arrowstyle="fancy"))
#
#ax4.plot(df.Year,df["Average Film Rating"])
#ax4.set_title("Average Film Rating",fontweight="bold",fontsize=10)
#
##%% show normalised values
#df_norm.plot(x="Year")

#%% CORRELATION BETWEEN FILM DURATION, RATING, AND NUMBER OF VOTES
#query = """
#select averageRating, numVotes, title_basics.runtimeMinutes from title_ratings
#join title_basics on title_basics.tconst=title_ratings.tconst
#where title_basics.titleType is "movie"
#group by title_basics.runtimeMinutes order by title_ratings.numVotes desc
#"""

query = """
select averageRating, numVotes, title_basics.runtimeMinutes from title_ratings
join title_basics on title_basics.tconst=title_ratings.tconst
where title_basics.titleType is "movie" and title_basics.runtimeMinutes is not "\\N";
"""

#path = r"C:\Users\omerzulal\Downloads\IMDB Databases\imdb_db_all.db"
path = r"C:\Users\omer.eker\Downloads\IMDB Databases\imdb_db_all.db"

#create a connection to the database
conn = sql.connect(path)

t1 = time.time()
#run the sql query using pandas function and store it into a dataframe
df = pd.read_sql_query(query,conn)
print("It took %.1f seconds"%(time.time-t1))

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


