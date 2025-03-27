import sqlite3
import requests
import json
from bs4 import BeautifulSoup

def task_1():
    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    weather_data = []
    rows = soup.find("table").find("tbody").find_all("tr")
    
    for row in rows:
        cols = row.find_all("td")
        day = cols[0].text
        temp = int(cols[1].text.replace("°C", ""))
        condition = cols[2].text
        weather_data.append({"day": day, "temperature": temp, "condition": condition})
    
    print("Weather Data:")
    for data in weather_data:
        print(data)
    
    max_temp = max(weather_data, key=lambda x: x["temperature"])
    sunny_days = [data["day"] for data in weather_data if data["condition"] == "Sunny"]
    avg_temp = sum([data["temperature"] for data in weather_data]) / len(weather_data)
    
    print("Hottest Day:", max_temp["day"])
    print("Sunny Days:", sunny_days)
    print("Average Temperature:", avg_temp)

def task_2():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    jobs = []
    for job in soup.find_all("div", class_="card-content"):
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="description").text.strip()
        apply_link = job.find("a", class_="apply")['href']
        jobs.append((title, company, location, description, apply_link))
    
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        apply_link TEXT,
        UNIQUE(title, company, location)
    )""")
    
    for job in jobs:
        cursor.execute("INSERT OR IGNORE INTO jobs (title, company, location, description, apply_link) VALUES (?, ?, ?, ?, ?)", job)
    conn.commit()
    conn.close()
    
    print("Job listings saved successfully.")

def task_3():
    url = "https://demoblaze.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    laptops = []
    items = soup.find_all("div", class_="card")
    
    for item in items:
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p", class_="card-text").text.strip()
        laptops.append({"name": name, "price": price, "description": description})
    
    with open("laptops.json", "w", encoding="utf-8") as file:
        json.dump(laptops, file, indent=4)
    
    print("Laptop data saved successfully in JSON format.")

if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
