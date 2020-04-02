![plot0](https://github.com/omerfarukeker/imdb_work/blob/master/header%20for%20linkedin2.png)
## Exploratory analysis on the IMDB movie database

Following Python codes generates some exploratory graphs to see the correlation between movie features. The IMDB movie database can be downloaded from the link below:

[IMDB Database](https://www.imdb.com/interfaces/)

The link also gives the description of the data.

I downloaded all .tsv files from the link and used all except "title.episode.tsv.gz" which has TV series data.

All .tsv files are imported into a SQLite database file (~4GB) and stored in the hardware. Python code are querying the necessary parts of the SQLite database and processing & visualising some interesting results.

Playing with data has always been a passion for me. It has been a long journey, more than 10 years. I have been dealing with variety of data; ranging from engineering data-sets like UAV fuel system data or a passenger aircraft wing structural health data to retail business or fun Kaggle data-sets.

Watching movies, talking about them and doing critics is another passion for me. And combining these two passions was hilarious. Recently, I made an exploratory data analysis on IMDb's movie database using one of the most frequently used data science programming language: Python.

I have always thought that 1994 is the year that best movies were made (Forrest Gump, Pulp Fiction, The Shawshank Redemption etc.). That's where this research idea was originated from.

The graph below contains two subplots, the former gives the total number of films made each year, and the latter gives total number of voters for the films made at corresponding year which was peaked in 2013 and a dramatic drop comes after. This is where the strange things started. Number of films made per year is increasing non-stop. Why people stop voting recent films? Is it because movies getting worse? Or is it IMDb website loosing its popularity? However it is obvious that IMDb still dominates online film rating sector as their mind blowing monthly visitor number reaches to 250 million [[read more]](https://www.businesswire.com/news/home/20180222005150/en/IMDb-Launches-First-Ever-Skill-Amazon-Alexa). 

<p align="center">
  <img src="https://github.com/omerfarukeker/imdb_work/blob/master/number%20of%20films%20and%20number%20of%20film%20voters.png">
</p>

This could be another research, we shall continue to find an answer to my original question:

> Was 1994 "the year" for the best films? 

The graph below gives the average values. The former displays the average voters per film again on a yearly basis, where the latter gives average film ratings per year. Since 1920s, average film ratings tend to fluctuate around 6/10. A slight increasing trend since late 80s is noticeable however the difference is not statistically significant to say films are getting better ratings. Average film rating graph still not answering the original question. 

<p align="center">
  <img src="https://github.com/omerfarukeker/imdb_work/blob/master/average%20voters%20vs%20average%20film%20rating.png">
</p>

If we examine the above graph with average voters per film, it was peaked at 90s and early 2000s and has been dropping dramatically. Film ratings are increasing but the number of votes per film is dropping? How could you explain that? This means to me that people tend to vote more when they liked a film. They don't bother rating a film which was average or boring. But this seem to apply for the recent films only, not 90s or 2000s films. Could we relate this to demographics, in particular the age of dominant voters? This is another point of research.

In summary, did this analysis satisfy my original assumption that the 1994 is "The year"? Yes, somehow did. Clearly the films made in the 90s and early 2000s are voted and gained attraction the most, where 1999 being the highest. 1994 is in the top 3.

Another interesting analysis result was the correlation between film duration and film rating. As seen in the figure below film rating is highly positively correlated with the film duration. The longer the film the higher likely to get higher ratings :) However the ratings start to fluctuate more for films having run times +3 hours and more.

<p align="center">
  <img src="https://github.com/omerfarukeker/imdb_work/blob/master/Film%20Runtime%20Stats%202.png">
</p>

I am looking forward to continue to work on this data to satisfy my data science desires on film data. Further analysis will be mainly focused on predictive analytics using machine learning algorithms. Any comments and recommendations are welcomed.

Cheers!
