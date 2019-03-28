# imdb_work
Exploratory analysis on the IMDB movie database

Following Python codes generates some exploratory graphs to see the correlation between movie features. The IMDB movie database can be downloaded from the link below:
https://www.imdb.com/interfaces/

The link also gives the description of the data.

I downloaded all .tsv files from the link and used all except "title.episode.tsv.gz" which has TV series data.

All .tsv files are imported into a SQLite database file (~4GB) and stored in the hardware. Python code are querying the necessary parts of the SQLite database and processing & visualising some interesting results. Let's go one by one:

I have always thought that 1994 is the year that best movies were made (Forrest Gump, Pulp Fiction, The Shawshank Redemption etc.). That's where this research was originated. 

The graph below contains 2 subplots, first one gives the number of films per year, second gives total number of voters per year which was peaked in 2013 and a dramatic drop comes after. This is where the strange things start. Why people stop voting? Is it because movies getting worse? Or is it IMDB that people move away from.

![plot1](https://github.com/omerfarukeker/imdb_work/blob/master/number%20of%20films%20and%20number%20of%20film%20voters.png)

The graph below gives the average values. First one displays the average voters per film again on a yearly basis, where the other gives average film ratings per year. Since 1920s average film ratings tend to fluctuate around 6/10. A slight increasing trend since late 80s is noticeable. However for me that doesn't mean that films are getting better. I believe people tend to vote more when they liked a film. If you look at the average voters per film, since early 2000s average number of votes per film is dropping drammatically.

![plot2](https://github.com/omerfarukeker/imdb_work/blob/master/average%20voters%20vs%20average%20film%20rating.png)

In summary, people tend to

I am looking forward to continue to work on this data as I am passionate about movies and data science. Recommendations are welcomed.

Cheers!
