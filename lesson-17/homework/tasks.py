import pandas as pd
import sqlite3
import numpy as np
# task1: INNER JOIN ON CHINOOK DB 

conn = sqlite3.connect('chinook.db')
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
customer_invoices = pd.merge(customers, invoices, on='CustomerId', how='inner')
invoice_counts = customer_invoices.groupby('CustomerId').InvoiceId.count().reset_index(name='TotalInvoices')
print(invoice_counts.head())

# task2: OUTER JOIN ON MOVIE DATA
movies = pd.read_csv('movie.csv')
df1 = movies[['director_name', 'color']]
df2 = movies[['director_name', 'num_critic_for_reviews']]
left_join = pd.merge(df1, df2, on='director_name', how='left')
outer_join = pd.merge(df1, df2, on= ' director name', how='outer')
left_join_rows = len(left_join)
outer_join_rows = len(outer_join)
print(f"Left Join Rows: {left_join_rows}")
print(f"Full Outer Join Rows: {outer_join_rows}")

# task3: GROUPING AND AGGREGATING ON TITANIC
titanic = pd.read_excel('titanic.xlsx')
filtered_titanic = titanic.groupby('Pclass')
avg_age = filtered_titanic['Age'].mean()
total_fare = filtered_titanic['Fare'].sum()
passenger_count = filtered_titanic['PassengerId'].count()
new_titanic = pd.DataFrame({
    'Pclass': filtered_titanic.groups.keys(),
    'Avg_Age': avg_age,
    'Total_Fare': total_fare,
    'Passenger_Count': passenger_count
})
print(new_titanic.head())

# task4: MULTI-LEVEL GROUPING ON MOVIES

grouped_movies = movies.groupby(['color', 'director_name']).agg({
    'num_critic_for_reviews': 'sum',
    'duration': 'mean'
}).reset_index()
print("Grouped Movies Data:")
print(grouped_movies.head())



# task5: NESTED GROUPING ON FLIGHTS
flights = pd.read_parquet('flights.parquet')
grouped_flights = flights.groupby(['Year', 'Month']).agg({
    'FlightNum': 'count',
    'ArrDelay': 'mean',
    'DepDelay': 'max'
}).rename(columns={'FlightNum': 'TotalFlights'}).reset_index()
print("Grouped Flights Data:")
print(grouped_flights.head())

# task6: APPLYING FUNCTIONS ON MOVIES
def age_group(age):
    if pd.isna(age):
        return np.nan
    return 'Child' if age < 18 else 'Adult'

titanic['Age_Group'] = titanic['Age'].apply(age_group)
print("Titanic with Age_Group:")
print(titanic[['Age', 'Age_Group']].head())

# task7: NORMALIZE EMPLOYEE SALARIES
employees = pd.read_csv('employee.csv')
employees['Normalized_Salary'] = employees.groupby('Department')['Salary'].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)
print("Normalized Employee Salaries:")
print(employees.head())

# task8: CUSTOM FUNCTION ON MOVIES
def classify_duration(duration):
    if pd.isna(duration):
        return np.nan
    elif duration < 60:
        return 'Short'
    elif duration <= 120:
        return 'Medium'
    else:
        return 'Long'
movies['Duration_Category'] = movies['duration'].apply(classify_duration)
print("Movies with Duration Category:") 
print(movies[['duration', 'Duration_Category']].head())

# task9: PIPELINE ON TITANIC

def filter_survivors(df):
    return df[df['Survived'] == 1]
def fill_age(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df
def add_fare_per_age(df):
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df
titanic_pipeline = (
    titanic
    .pipe(filter_survivors)
    .pipe(fill_age)
    .pipe(add_fare_per_age)
)
print("Titanic Pipeline Result:")
print(titanic_pipeline[['Survived', 'Age', 'Fare_Per_Age']].head())

# task10: PIPELINE ON FLIGHTS
def filter_delays(df):
    return df[df['DepDelay'] > 30]
def add_delay_per_hour(df):
    df['Delay_Per_Hour'] = df['DepDelay'] / df['AirTime']
    return df
flights_pipeline = (
    flights
    .pipe(filter_delays)
    .pipe(add_delay_per_hour)
)
print("Flights Pipeline Result:")
print(flights_pipeline[['DepDelay', 'AirTime', 'Delay_Per_Hour']].head())

