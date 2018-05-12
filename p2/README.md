# P2: Investigate a TMDb Movie Dataset
## Overview
In this project, I analyzed the TMDb movie dataset by using Python libraries NumPy, pandas, and Matplotlib. The dataset, which is originally from [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata/data), was cleaned and provided by Udacity. The dataset contains 5000+ movies basic information and some metrics that measured can be classified how successful these movies are. These metrics include popularity, revenue and vote average. Basic information are like cast, director, keywords, runtime, genres, etc. 

Since it contains plentiful information, the project I investigated is focus on finding properties are associated with successful movies. Besides I also investigated some interesting trends like keywords trends by generation. For more investigation questions, see [Question Researched](#question-researched).

The project primary goal is to go through the general data analysis process, so the project report is including four parts: 
- questions asking 
- data wrangling 
- exploratory data analysis 
- conclusion

See my findings in the [Jupyter Notebook](https://github.com/onpillow/Udacity-DAND-Term1/blob/master/p2/Investigate_a_Dataset.ipynb)!

## Question Researched
### Part 1: General Explore
- Question 1: Popularity Over Years
- Question 2: The distribution of revenue in different popularity levels in recent five years.
- Question 3: The distribution of revenue in different score rating levels in recent five years.
### Part 2: Find the Properties are Associated with Successful Movies
- Question 1: What kinds of properties are associated with movies that have high popularity?
- Question 2: What kinds of properties are associated with movies that have high voting score?
### Part 3: Top Keywords and Genres Trends by Generation
- Question 1: Number of movie released year by year
- Question 2: Keywords Trends by Generation
- Question 3: Genres Trends by Generation

## My findings
-  The movie popularity trend is growing from 1960 on average.
-  Movies with higher revenue level are with higher popularity in recent five years on average. 
-  Movies with higher revenue level don't have the significant high score rating in recent five years. 
- High popularity movies are with high budget levels and longer run time.
- Among top 100 high voting score movies in each year, I found out top three properties of them:

|Top| Director | Genres | Keywords |   
| ------ | ------ | ------ | ------ |   
|1| Woody Allen | Drama | based on novel |
|2| Martin Scorsese | Comedy | 	independent film |
|3| Clint Eastwood | Thriller | woman director |
- Keywords and genres trends by generation

Keywords Trends            |  Genres Trends
:-------------------------:|:-------------------------:
![image](https://github.com/onpillow/Udacity-DAND-Term1/blob/master/p2/result_image/keyword_trend.png)  |  ![image](https://github.com/onpillow/Udacity-DAND-Term1/blob/master/p2/result_image/genres_trends.png)

For more details and ideas, check out my blog [article](https://medium.com/@onpillow/01-investigate-tmdb-movie-dataset-python-data-analysis-project-part-1-data-wrangling-3d2b55ea7714).
## License
[MIT License](https://github.com/onpillow/Udacity-DAND-Term1/blob/master/p2/LICENSE)
