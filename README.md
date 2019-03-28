# imdb_work
Exploratory analysis on the IMDB movie database

Following Python codes generates some exploratory graphs to see the correlation between movie features. The IMDB movie database can be downloaded from the link below:
https://www.imdb.com/interfaces/

The link also gives the description of the data.

I downloaded all .tsv files from the link and used all except "title.episode.tsv.gz" which has TV series data.

All .tsv files are imported into a SQLite database file (~4GB) and stored in the hardware. Python code are querying the necessary parts of the SQLite database and processing & visualising some interesting results. Let's go one by one:

I have always thought that 1994 is the year that best movies were made (Forrest Gump, Pulp Fiction, The Shawshank Redemption etc.). That's where this research was originated. The graph below contains 4 subplots, first one gives the number of films per year, second gives total number of voters per year which was peaked in 2013 and a dramatic drop comes after. This is where the strange things start. Why people stop voting? Is it because movies getting worse? or it is IMDB that people move away.
![allinonesubplots](https://github.com/omerfarukeker/imdb_work/blob/master/all%20in%20one%20results%20subplot.png)

Let's discuss the bottom 2 plots altogether. First one gives the average voters per film again on a yearly basis, where the other gives average film ratings per year. Since 1920s average film ratings tend to flow around 6/10. A slight increasing trend since late 80s can be seen too. However 


![normalised](https://github.com/omerfarukeker/imdb_work/blob/master/all%20in%20one%20results%20normalised.png)

I am looking forward to continue to work on this data as I am passionate about movies and data science. Recommendations are welcomed.

Cheers!
