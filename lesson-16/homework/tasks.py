# Part 1: reading files

# task1 : chinook.db
import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')

customers_df = pd.read_sql_query("SELECT * FROM customers", conn)

print(customers_df.head(10))

# task2 : iris.json
iris_df = pd.read_json('iris.json')

print(iris_df.shape)
print(iris_df.columns.tolist())

# task3 : titanic.xlsx
titanic_df = pd.read_excel('titanic.xlsx')
print(titanic_df.head())

#  task4 : Flights parquet file
flights_df = pd.read_parquet('flights.parquet')
print(flights_df.info())

# task5 : movie.csv
movies_df = pd.read_csv('movie.csv')
print(movies_df.sample(10))

#  Part 2: Exploring DataFrames
# task1 : Using the DataFrame from iris.json
iris_df.columns = iris_df.columns.str.lower()
iris_subset = iris_df[['sepal_length', 'sepal_width']]
print(iris_subset.head())

# task2: From the titanic.xlsx DataFrame
titanic_over_30 = titanic_df[titanic_df['Age'] > 30]
print(titanic_over_30.head())

print(titanic_df['Gender'].value_counts())

# task3: From the flights parquet file
flights_df_subset = flights_df[['Carrier', 'Origin', 'Dest']]
print(flights_df_subset.head())

unique_dest = flights_df['Dest'].nunique()
print(unique_dest)

# task4: From the movie.csv file
movies_over_120min = movies_df[movies_df['Duration'] > 120]
print(movies_over_120min.head())

sorted_long_movies = movies_over_120min.sort_values('director_facebook_likes', ascending=False)
print(sorted_long_movies)

# Part 3: Challenges and Explorations
print(iris_df.describe().loc[['mean', '50%', 'std']])

print(titanic_df['Age'].agg(['min', 'max', 'sum']))

top_director = movies_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
print(top_director)

longest_movies = movies_df[['movie_title', 'duration', 'director_name']].sort_values('duration', ascending=False).head(5)
print(longest_movies)

print(flights_df.isnull().sum())

if 'air_time' in flights_df.columns:
    flights_df['air_time'].fillna(flights_df['air_time'].mean(), inplace=True)
