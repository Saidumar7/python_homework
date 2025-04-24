import requests
import random

# Task 1: Weather API
def get_weather(city):
    api_key = "api_key" 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print("Error fetching weather data.")

# Task 2: Movie Recommendation System
def get_movie_recommendation(genre):
    api_key = "api_key"  
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre}"
    response = requests.get(url)
    data = response.json()
    if "results" in data and data["results"]:
        movie = random.choice(data["results"])
        print(f"Recommended Movie: {movie['title']}")
        print(f"Overview: {movie['overview']}")
    else:
        print("No movies found for this genre.")

# Example Usage
if __name__ == "__main__":
    city = "Tashkent"
    get_weather(city)
    
    genre = input("Enter movie genre (e.g., action, comedy, drama): ")
    get_movie_recommendation(genre)
